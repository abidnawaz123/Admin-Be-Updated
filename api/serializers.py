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