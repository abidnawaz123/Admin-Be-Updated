from .models import *
from rest_framework import serializers

class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'id','first_name', 'last_name', 'email', 'status']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadModel
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    lead = serializers.SerializerMethodField()
    assigned_lead = serializers.PrimaryKeyRelatedField(
        queryset=LeadModel.objects.all(), write_only=True, allow_null=True, required=False
    )
    assigned_employee = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = ProjectModel
        fields = ['name', 'description', 'lead', 'assigned_lead', 'assigned_employee']

    def get_lead(self, obj):
        lead_name = obj.assigned_lead.name if obj.assigned_lead else None
        team = [
            {
                "employee_name": f"{emp.first_name} {emp.last_name}".strip(),
                "employee_status": emp.status
            }
            for emp in obj.assigned_employee.all()
        ]
        return {
            "name": lead_name,
            "team": team
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

    def get_assigned_employee(self, obj):
        return CustomUsersSerializer(obj.assigned_employee.all(),many=True).data


    # def get_assigned_employee(self,obj):
    #     return EmployeeSerializer(obj.assigned_employee.all(),many=True).data

    def get_assigned_project(self, obj):
        return obj.assigned_project.name

    def get_tags(self, obj):
         return [tag.name for tag in obj.tags.all()]
