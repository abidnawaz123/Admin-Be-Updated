from rest_framework import generics
from .models import *
from .serializers import EmployeeSerializer, ProjectSerializer, TicketHeadingsSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from myapp.models import CustomUser


class EmployeeView(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class ProjectView(generics.ListAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class TicketHeadingsView(generics.ListAPIView):
    queryset = TicketHeadings.objects.all()
    serializer_class = TicketHeadingsSerializer


class AssignedProjectToEmployeeView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract the employee name from query parameters
        employee_name = request.query_params.get('employee_name')

        if not employee_name:
            return Response({"error": "Employee name is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Query the projects assigned to the employee
        projects = ProjectModel.objects.filter(assigned_employee__name=employee_name)

        project_data = []

        # Building response data
        for project in projects:
            lead = project.assigned_lead
            lead_data = {
                "name": lead.name if lead else None,
                "team": [employee.name for employee in lead.lead_team.all()] if lead else []
            }

            project_data.append({
                "name": project.name,
                "description": project.description,
                "lead": lead_data
            })

        if not project_data:
            return Response({"message": "No projects found for the given employee"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"projects": project_data}, status=status.HTTP_200_OK)
