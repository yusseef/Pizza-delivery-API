from django.urls import path
from .views import *
urlpatterns = [
    path('', HelloOrders.as_view(), name = 'hello_order')
]