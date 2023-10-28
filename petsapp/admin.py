from django.contrib import admin
from . models import Pets,Author,Book,Course
from cart.models import Cart
from django.utils.html import format_html
from orders.models import Orders,OrderPet,Payment
from cart.models import Cart


class OrderCustom(admin.ModelAdmin):
    list_display = ['user','status']

class PaymentCustom(admin.ModelAdmin):
    list_display = ['payment_id','status']

class CustomAdmin(admin.ModelAdmin):
    list_display = ['img_display','name','gender','animal_type','price','species','desc','age']
    list_filter = ['animal_type','gender']
    search_fields = ['species','age','gender']
    list_per_page = 10

    def img_display(self,obj):
        return format_html('<img src={} width="90" height="90" />',obj.image.url)

# Register your models here.
#any admin related changes can be done there

admin.site.register(Pets,CustomAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Cart)
admin.site.register(Orders,OrderCustom)
admin.site.register(OrderPet)
admin.site.register(Payment,PaymentCustom)

