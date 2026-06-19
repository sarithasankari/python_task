from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class StudentView(APIView):
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data is added")
        return Response(serializer.errors)

    def get(self,request,id=None):
        if id is None:
            d=Student.objects.all()
            serializer=StudentSerializer(d,many=True)
            return Response(serializer.data)
        else:
            d=Student.objects.get(id=id)
            serializer=StudentSerializer(d)
            return Response(serializer.data)
    
    def patch(self,request,id):
        d=Student.objects.get(id=id)
        serializer=StudentSerializer(d,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data is updated")
        return Response(serializer.errors)
    
    def put(self,request,id):
        d=Student.objects.get(id=id)
        serializer=StudentSerializer(d,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data is updated")
        return Response(serializer.errors)

    def delete(self,request,id):
        n=Student.objects.get(id=id)
        n.delete()
        return Response("data is deleted")
      
