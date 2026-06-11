from django.shortcuts import render,redirect
from .models import *

def home(request):
    students=Student.objects.all()

    return render(request,'home.html',{'students':students})



def user(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        course=request.POST.get('course')
        Student.objects.create(
            name=name,
            age=age,
            course=course,
        )
        return redirect('home')

    return render(request,'user.html')