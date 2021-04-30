# from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm # new to line\\
from django.urls import reverse_lazy                    # new
from django.views import generic


class SignUpView(generic.CreateView): # new
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

