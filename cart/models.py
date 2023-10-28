from django.db import models
from petsapp.models import Pets #when we are adding anything in cart we need to get the data from already made model. 
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=200,blank=True)
    pet = models.ForeignKey(Pets,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalPrice = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_tbl'



