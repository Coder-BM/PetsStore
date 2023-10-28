from django import forms

from .models import Orders,Payment,OrderPet


class OrderForm(forms.ModelForm):
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

    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(max_length=100,
                                 widget=forms.Select(choices=states,attrs={'class':'form-control'}))
    country = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Orders
        fields = ['first_name','last_name','phone','email','address','city','state','country']