from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class StudentView(APIView):
    def get(self,request , id='None'):
        if id =='None':
            task=Student.objects.all()
            serializer=StudentSerializer(task,many=True)
            return Response(serializer.data)
        else:
            task=Student.objects.get(id=id)
            serializer=StudentSerializer(task)
            return Response(serializer.data)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("New Task Added")
        return Response(serializer.errors)
    