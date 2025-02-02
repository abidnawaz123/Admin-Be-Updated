# api/admin.py
from django.contrib import admin
from .models import *
from .CustomAdminForm import EmployeeForm
# Register the EmployeeModel in the admin interface
# admin.site.register(EmployeeModel)

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm

admin.site.register(LeadModel)
admin.site.register(ProjectModel)
admin.site.register(TicketModel)
admin.site.register(TicketHeadings)
admin.site.register(TicketTags)