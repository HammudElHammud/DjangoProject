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
        return self.product


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


