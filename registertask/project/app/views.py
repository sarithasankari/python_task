from django.shortcuts import render, redirect
from .models import StudentModule


# Create your views here.
def StudentView(request):
    if request.method == "POST":
        StudentModule.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            age=request.POST.get("age")
        )

        return redirect("list")

    return render(request, "request.html")


def StudentList(request):
    data = StudentModule.objects.all()
    return render(request, "list.html", {"data": data})