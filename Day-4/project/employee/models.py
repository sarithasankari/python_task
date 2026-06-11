from django.db import models

# Create your models here.
class Employee(models.Model):
     Employee_Name=models.CharField(max_length=100) 
     Department=models.CharField(max_length=100) 
     Salary = models.IntegerField()

     def __str__(self):
        return self.Employee_Name