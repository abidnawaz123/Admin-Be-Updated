from rest_framework import generics
from .models import *
from .serializers import ProjectSerializer, TicketSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from myapp.models import CustomUser


# class EmployeeView(generics.ListAPIView):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = EmployeeSerializer

class ProjectView(generics.ListAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class AssignedProjectToEmployeeView(APIView):

    def get(self, request, *args, **kwargs):
        # Extract the employee name from query parameters
        employee_id = request.query_params.get('employee_id')
        is_admin = request.query_params.get('is_admin')

        if not employee_id:
            return Response({"error": "Employee id is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Query the projects assigned to the employee
        projects = ProjectModel.objects.filter(assigned_employee__id=employee_id) if not is_admin else ProjectModel.objects.all()

        project_data = []

        # Building response data
        for project in projects:
            lead = project.assigned_lead
            lead_data = {
                "name": lead.name if lead else None,
                "team": [{
                    "employee_name":employee.get_full_name(),
                    "employee_status": employee.status
                } for employee in project.assigned_employee.all()] if project.assigned_employee else []
            }

            project_data.append({
                "name": project.name,
                "description": project.description,
                "lead": lead_data
            })

        if not project_data:
            return Response({"message": "No projects found for the given employee"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"projects": project_data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AssignedTickets(APIView):
    def get(self, request, *args, **kwargs):
        try:
            employee_id = request.query_params.get('employee_id')

            if not employee_id:
                return Response({"error": "Employee id is required"}, status=status.HTTP_400_BAD_REQUEST)

            ticket = TicketModel.objects.filter(assigned_employee=employee_id)

            serializer = TicketSerializer(ticket, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Exception({"error": "Ticket not found"}, status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            ticket_id = kwargs.get("pk")
            payload_data = request.data
            if not ticket_id:
                return Response({"error": "Ticket id is required"}, status=status.HTTP_400_BAD_REQUEST)
            updated_data = TicketModel.objects.filter(id=ticket_id).update(**payload_data)
            if not updated_data:
                return Response({"message": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)
            updated_ticket = TicketModel.objects.get(id=ticket_id)
            serializer = TicketSerializer(updated_ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            raise Exception({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
