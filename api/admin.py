# api/admin.py
from django.contrib import admin
from .models import *

# Register the EmployeeModel in the admin interface
admin.site.register(EmployeeModel)
admin.site.register(LeadModel)
admin.site.register(ProjectModel)