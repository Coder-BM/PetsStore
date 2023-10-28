from django.urls import path
from .views import add_to_cart,update_cart
from . import views

urlpatterns = [
path("add_to_cart/<int:id>",add_to_cart,name="add_to_cart"),
path('cart',views.cart,name='cart'),
path('cartpage',views.cart_home,name='cartpage'),
path('delete/<int:id>',views.delete,name='delete'),
path('updatecart/<int:id>/',update_cart,name='updatecart'),

]