from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'age']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadModel
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):

    assigned = serializers.SerializerMethodField()

    class Meta:
        model = ProjectModel
        fields = ['name','description','assigned']

    def get_assigned(self, obj):
        return {
            "lead_name": obj.assigned_lead.name,
            "lead_team": obj.assigned_lead.lead_team.all().values('name', 'age')
        }

class TicketSerializer(serializers.ModelSerializer):
    assigned_lead = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    assigned_employee = serializers.SerializerMethodField()
    assigned_project = serializers.SerializerMethodField()

    class Meta:
        model = TicketModel
        fields = "__all__"
    def get_assigned_lead(self, obj):
        return {
            "lead_name": obj.assigned_lead.name,
        }

    def get_assigned_employee(self,obj):
        return EmployeeSerializer(obj.assigned_employee.all(),many=True).data

    def get_assigned_project(self, obj):
        return obj.assigned_project.name

    def get_tags(self, obj):
         return [tag.name for tag in obj.tags.all()]

class TicketHeadingsSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=True)
    class Meta:
        model = TicketHeadings
        fields = "__all__"