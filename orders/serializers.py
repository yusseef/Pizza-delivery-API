from . models import Order
from rest_framework import serializers

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['size', 'flavour', 'quantity']

class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_status']

