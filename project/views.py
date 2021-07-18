from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, "index.html")

# def registration_page(request):
#     # 'form'=UserCreationForm
#     # ctx={

#     # }
#     return render(request, 'registration/register.html')





