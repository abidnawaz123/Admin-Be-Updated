# from django import forms
# # from .models import EmployeeModel
# from django.contrib.auth import get_user_model
#
# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeModel
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         User = get_user_model()
#         self.fields['user'].queryset = User.objects.filter(role='employee')
#
#     def clean_user(self):
#         user = self.cleaned_data.get('user')
#
#         # Allow the same user if updating the same record
#         if self.instance.pk:
#             existing_employee = EmployeeModel.objects.filter(user=user).exclude(pk=self.instance.pk)
#             if existing_employee.exists():
#                 raise forms.ValidationError("This user is already assigned as an employee.")
#         else:
#             # Handle creation scenario
#             if EmployeeModel.objects.filter(user=user).exists():
#                 raise forms.ValidationError("This user is already assigned as an employee.")
#
#         return user
