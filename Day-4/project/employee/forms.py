from django import forms
from .models import Employee


class EmployeeForm(forms.modelForm):
    class Meta:
        model=Employee
        fields='__all__()'

        