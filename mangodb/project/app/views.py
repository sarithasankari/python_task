from django.shortcuts import render
from django.http import HttpResponse
from app.mongodb import users_collection


def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = {
            "name": name,
            "email": email,
            "password": password
        }

        users_collection.insert_one(user)

        return render(request, "register.html", {"success": True})

    return render(request, "register.html")