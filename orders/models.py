from django.db import models

from petsapp.models import Pets

from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id
    
class Orders(models.Model):
    status = (("new",'new'),
              ('pending','pending'),
              ('delivered','delivered'),
              ('cancelled','cancelled'))
    
    states = [
        ('AP',"Andhra Pradesh"),
        ('AR',"Arunachal Pradesh"),
        ('AS',"Assam"),
        ('BR',"Bihar"),
        ('Goa',"Goa"),
        ('GJ',"Gujurat"),
        ('RJ',"Rajasthan"),
        ('MH',"Maharashtra"),
        ('UP',"Uttar Pradesh")
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=states,default='MH')
    country = models.CharField(max_length=100)
    total = models.FloatField()
    status = models.CharField(max_length=100,choices=status,default='new')
    ip = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add to store new object
    updated_at = models.DateField(auto_now=True) #auto_now to store object that is already created

    def __str__(self):
        return self.first_name
    

class OrderPet(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    pet = models.ForeignKey(Pets,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    pet_price = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.pet.name