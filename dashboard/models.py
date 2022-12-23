from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Category=(
    ('Electronics','Electronics'),
    ('Books','Books'),
    ('Food','Food'),
)
class Product(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,choices=Category,null=True,blank=True)
    quantity=models.PositiveBigIntegerField(null=True,blank=True)

    class Meta:
        verbose_name_plural="Product"

    def __str__(self):
        return f'{self.name} - {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Order" #Customize table name

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
