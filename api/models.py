from django.db import models

from myapp.models import CustomUser
from .managers import EmployeeManager
from django.conf import settings


# class EmployeeModel(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='employee_profile',unique=True,null=True,blank=True)
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(default=0)
#
#     objects = EmployeeManager()
#
#     def __str__(self):
#         return self.name

class LeadModel(models.Model):
    name = models.CharField(max_length=100)
    lead_team = models.ManyToManyField(CustomUser, related_name='lead_team')
    def __str__(self):
        return self.name

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ProjectModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    assigned_lead = models.ForeignKey(LeadModel,on_delete=models.CASCADE,null=True,blank=True)
    assigned_employee = models.ManyToManyField(CustomUser)
    def __str__(self):
        return self.name

class TicketTags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TicketModel(models.Model):

    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    heading = models.CharField(max_length=300)
    number = models.IntegerField()
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=100)
    assigned_lead = models.ForeignKey(LeadModel,on_delete=models.CASCADE,null=True,blank=True)
    assigned_project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,null=True,blank=True)
    assigned_employee = models.ManyToManyField(CustomUser,related_name='assigned_employee')
    priority = models.CharField(choices=PRIORITY_CHOICES,default='low',max_length=10)
    time_estimated = models.DateTimeField(auto_now_add=True)
    date_to_complete = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TicketTags, related_name='ticket_tags',null=True,blank=True)

    extra_fields = models.JSONField(default=dict,null=True,blank=True)

    def __str__(self):
        return f'{self.number} {self.heading}'
