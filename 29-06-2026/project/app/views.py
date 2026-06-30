from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView


# Create your views here.
class StudentView(APIView):
    def post(self,request):
        task=StudentSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response("task is added")
        else:
            return Response(task.errors)

    def get(self,request,id=None):
        if id is None:
            task=StudentModel.objects.all()
            data=StudentSerializer(task,many=True)
            return Response(data.data)
        else:
            task=StudentModel.objects.get(id=id)
            data=StudentSerializer(task)
            return Response(data.data)
    
    def patch(self,request,id):
        data=StudentModel.objects.get(id=id)
        task=StudentSerializer(data,data=request.data,partial=True)
        if task.is_valid():
            task.save()
            return Response(task.data)
        else:
            return Response(task.errors)

    def put(self,request,id):
        data=StudentModel.objects.get(id=id)
        task=StudentSerializer(data,data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data)
        else:
            return Response(task.errors)

    def delete(self,request,id):
        data=StudentModel.objects.get(id=id)
        data.delete()
        return Response("data is deleted")




        

        
