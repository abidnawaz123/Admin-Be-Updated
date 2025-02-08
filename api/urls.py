from django.urls import path
from .views import *

urlpatterns = [
    # path('employee/', EmployeeView.as_view(), name='employee-list-create'),
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('assignedproject/',AssignedProjectToEmployeeView.as_view(), name='assigned-project-to-employee-list'),
    path('assigned_tickets/',AssignedTickets.as_view(), name='assigned-tickets-list'),
    path('assigned_tickets/<int:pk>', AssignedTickets.as_view(), name='assigned-tickets-list'),
]