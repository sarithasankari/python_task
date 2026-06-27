from django.shortcuts import render, redirect
from django.contrib import messages
from pymongo import MongoClient
from django.contrib.auth.hashers import make_password

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users_collection = db["users"]


def register(request):
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        existing_user = users_collection.find_one(
            {"username": username}
        )

        if existing_user:
            messages.error(request, "Username already exists")
            return redirect("register")

        existing_email = users_collection.find_one(
            {"email": email}
        )

        if existing_email:
            messages.error(request, "Email already exists")
            return redirect("register")

        hashed_password = make_password(password)

        users_collection.insert_one({
            "full_name": full_name,
            "email": email,
            "username": username,
            "password": hashed_password,
        })

        messages.success(request, "Registration Successful")
        return redirect("register")

    return render(request, "register.html")