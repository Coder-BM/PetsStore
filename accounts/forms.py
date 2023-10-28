from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #auth user table 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        #__all__ if we need all columns
        fields = ['username','email','first_name','last_name','password1','password2','check'] 

    username = forms.CharField(max_length=100, 
                               required=True, 
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'User Name'}))
    
    email = forms.EmailField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email Address'}))
    
    first_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    
    password1 = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Password','type': 'password'}))
    
    password2 = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Confirm Password','type': 'password'}))

    check = forms.BooleanField(required=True) 
                                