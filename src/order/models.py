from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from forSale.models import Forslar

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Forslar,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


    @property
    def amount(self):
        return (self.quantity * self.product.pric)

    @property
    def price(self):
        return (self.product.pric)

class ShopCartForm(ModelForm):
    class Meta:
      models = ShopCart
      fields = ['quantity']





class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('prepare','prepare'),
        ('onShopping','onShopping'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=202,blank=True)
    city = models.CharField(max_length=20,blank=True)
    total = models.FloatField(max_length=20,blank=True)
    country = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=20,blank=True,choices=STATUS,default='New')
    ip = models.CharField(max_length=20,blank=True,)
    adminnote = models.CharField(max_length=202,blank=True,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.first_name



class OrderForm(ModelForm):
    class Meta:
        models = Order
        fields =['first_name','last_name','address','city','country','phone']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Forslar, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20,blank=True,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name

