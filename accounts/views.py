from typing import Optional
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import RegistrationForm

from django.contrib import messages

from petsapp.views import pets_list

from django.contrib.auth.views import LoginView,LogoutView

from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,"base/register.html",{'form':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST) #will get all the fields in forms.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #cleaned_data will 
            messages.success(request,"Account Created Successfully for" +" " + username)
            return redirect(pets_list)
        else:
            messages.error(request,"Some Error..")
            return render(request,'base/register.html',{'form':form})
        
    # return render(request,"base/register.html",{"form":form})


class MyLoginView(LoginView):
    def form_valid(self,form): #this form is not the Registration form created above but the authethication form which is in Django
        messages.success(self.request,"Logged In Successfully")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"Invalid Credentials.")
        return super().form_invalid(form)
    

#if we use class redirect wont work we need to use reverse lazy

class MyLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')






