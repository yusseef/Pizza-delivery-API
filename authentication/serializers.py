from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.hashers import make_password

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number']

    def validate(self, attrs):
        username_exist = User.objects.filter(username = attrs['username']).exists()
        if username_exist:
            raise ValidationError(detail = 'User with username already exists')
        
        email_exist = User.objects.filter(email = attrs['email']).exists()
        if email_exist:
            raise ValidationError(detail = 'User with email already exists')

        phone_number_exist = User.objects.filter(phone_number = attrs['phone_number']).exists()
        if phone_number_exist:
            raise ValidationError(detail = 'User with phone_number already exists')

        return super().validate(attrs)
