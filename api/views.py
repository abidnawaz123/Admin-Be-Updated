from rest_framework import generics
from .models import *
from .serializers import EmployeeSerializer, ProjectSerializer, TicketHeadingsSerializer


class EmployeeView(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class ProjectView(generics.ListAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class TicketHeadingsView(generics.ListAPIView):
    queryset = TicketHeadings.objects.all()
    serializer_class = TicketHeadingsSerializer