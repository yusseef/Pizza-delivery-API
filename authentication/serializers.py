from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length = 8)

    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number']

    def validate(self, attrs):
        username_exist = User.objects.filter(username = attrs['username']).exists()
        if username_exist:
            raise serializers.validationerror(details = 'User with username already exists')
        
        email_exist = User.objects.filter(email = attrs['email']).exists()
        if email_exist:
            raise serializers.validationerror(details = 'User with email already exists')

        phone_number_exist = User.objects.filter(phone_number = attrs['phone_number']).exists()
        if phone_number_exist:
            raise serializers.validationerror(details = 'User with phone_number already exists')

        return super().validate(attrs)