from django.db import models


class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class LeadModel(models.Model):
    name = models.CharField(max_length=100)
    lead_team = models.ManyToManyField(EmployeeModel, related_name='lead_team')
    def __str__(self):
        return self.name

class ProjectModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    assigned_lead = models.ForeignKey(LeadModel,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name