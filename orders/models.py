from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Order(models.Model):
    SIZES  = (
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
    )    
    ORDER_STATUS = (
        ('pending', 'pending'),
        ('in transit', 'in transit'),
        ('delivered', 'delivered'),
    )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices = SIZES)
    order_status = models.CharField(max_length=50, choices = ORDER_STATUS)
    flavour = models.CharField(max_length=200)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'Order number {self.id} ======> {self.flavour} {self.size} by {self.customer} '