from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserCreationSerializer
# Create your views here.

class HelloAuth(APIView):
    def get(self, request):
        return Response({'message': 'Hello'}, status = status.HTTP_200_OK)


class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserCreationSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = UserCreationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)