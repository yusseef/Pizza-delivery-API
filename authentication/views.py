from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User
from .serializers import UserCreationSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class HelloAuth(APIView):
    def get(self, request):
        return Response({'message': 'Hello'}, status = status.HTTP_200_OK)


class UserView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer
    @swagger_auto_schema(operation_summary= "Create Users")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)