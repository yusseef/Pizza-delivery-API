from django.urls import path
from .views import *
urlpatterns = [
    path('', HelloOrders.as_view(), name = 'hello_order'),
    path('list/', OrderCreateSerliazer().as_view(), name = 'order_listcreate'),
    path('list/<str:id>/', OrderPkSerializer().as_view(), name = 'order_pk'),
    path('updatestatus/<str:id>/', UpdateOrderStatusView().as_view(), name = 'order_status'),
    path('customerorder/', UserOrdersView().as_view(), name = 'user_orders'),




]