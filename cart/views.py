from django.shortcuts import render,redirect
from .models import Cart
from petsapp.models import Pets
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.

def add_to_cart(request,id):
    cart_id = request.session.session_key # for storing sessions key in cart
    if cart_id == None: #check for cart id if none 
        cart_id = request.session.create()
    
    pet_data = Pets.objects.get(id=id)
    price = pet_data.price
    user_data = request.user
    Cart(cart_id=cart_id,pet=pet_data,user=user_data,totalPrice=price).save()
    messages.success(request,"Item Added To Cart Successfully")
    return redirect('/')

def cart(request): #done by blaise
    user = request.user
    a =Cart.objects.filter(user=user)
    d = {'objects':a} 
    return render(request,"petsapp/cart.html",d)

def cart_home(request): #done by sir
    all_items = Cart.objects.filter(user=request.user)
    flag = all_items.exists()
    return render(request,'cart/cart_home.html',{'items':all_items,'flag':flag})

def delete(request,id):
    a = Cart.objects.get(id=id)
    a.delete()
    messages.success(request,"Item Removed from Cart Successfully.")
    return redirect('cartpage')

def update_cart(request,id):
    p = request.POST.get('price')
    q = request.POST.get('qty')
    p_id = request.POST.get('id')
    total_price = float(p)*float(q)
    Cart.objects.filter(id=p_id).update(quantity=q,totalPrice=total_price)
    total_amount = Cart.objects.filter(user=request.user).aggregate(total=Sum('totalPrice'))['total'] or 0.0 #sql .aggregate ['total] is the django syntax for storing totalPrice
    return JsonResponse({'status':True, 'totalprice':total_price,'totalamount':total_amount})