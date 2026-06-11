from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def employee(request):
    employee=Employee.objects.all()
    return render(request,'employee_table.html',{'employee':employee})

def empss(request):
    if request.method=='POST':
        employee_name=request.POST.get('Employee')
        department=request.POST.get('Department')
        salary=request.POST.get('Salary')

        Employee.objects.create(
            Employee_Name=employee_name,
            Department=department,
            Salary=salary,
        )

        return redirect('employee_table')
    return render(request,'employee.html')