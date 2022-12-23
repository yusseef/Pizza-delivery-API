from django.urls import path
from .views import *
urlpatterns = [

    path('users/', UserView.as_view(), name = 'user_view'),
]