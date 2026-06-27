from django.shortcuts import render
from .mongodb import user_collection

# Create your views here.
def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user={
            'name':name,
            'email':email,
            'password':password
        }
        user_collection.insert_one(user)
        return render(request,'register.html',{'success':True})
    return render(request,"register.html")

    