
from django.urls import path
from . import views

urlpatterns = [
    path('emp/',views.empss,name='empss'),
    path('employee_table/',views.employee,name='employee_table'),
]