from django.urls import path
from .views import *

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name='employee-list-create'),
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('tickets/', TicketHeadingsView.as_view(), name='ticket-headings-list'),
]