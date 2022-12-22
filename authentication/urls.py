from django.urls import path
from .views import *
urlpatterns = [
    path('', HelloAuth.as_view(), name = 'hello_auth')
]