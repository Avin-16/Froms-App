from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
class Question(APIView):
    def get(self):
        query=Question.objects.all()
        serializer = QuestionSerializers(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )
    
    def post(self,request):
        data = request.data
        serializer = QuestionSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class Choice(APIView):
    def post(self,request):
        incoming_data= request.data
        serializer= ChoicesSerializers(data=incoming_data,many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"message": "Choices posted successfully!"}, status=status.HTTP_201_CREATED)


