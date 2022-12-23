from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['flavour', 'size', 'customer', 'order_status', 'created_at']
    list_filter = ['order_status', 'created_at']
    
admin.site.register(Order, OrderAdmin)