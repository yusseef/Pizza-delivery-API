from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class HelloAuth(APIView):
    def get(self, request):
        return Response({'message': 'Hello'}, status = status.HTTP_200_OK)
