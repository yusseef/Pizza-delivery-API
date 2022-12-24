from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . models import Order
from .serializers import OrderSerializer, OrderGetSerializer, StatusOrderSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HelloOrders(APIView):
    def get(self, request):
        return  Response({'message': 'Helloorders'}, status = status.HTTP_200_OK)

class OrderCreateSerliazer(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderGetSerializer(order, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data  = request.data)
        user  = request.user
        if serializer.is_valid():
            serializer.save(customer =  user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_204_NO_CONTENT)


class OrderPkSerializer(APIView):
    def get_object(self, id):
        try:
            return Order.objects.get(id = id)
        except Order.DoesNotExist:
            raise Http404
    def get(self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = self.get_object(id)
        order.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class UpdateOrderStatusView(APIView):
    def get_object(self, id):
        try:
            return Order.objects.get(id = id)
        except Order.DoesNotExist:
            raise Http404

    def put(self,request, id):
        order = self.get_object(id)
        serializer = StatusOrderSerializer(order, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)


class UserOrdersView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        order = Order.objects.all().filter(customer = user)
        serializer = OrderGetSerializer(order, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
