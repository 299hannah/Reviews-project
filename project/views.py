from django.shortcuts import render, redirect
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib import messages
from .models import UserProfile
# Create your views here.

def index(request):
	return render(request, "index.html")

def profile_view(request):
    logged_user=request.user
    user=UserProfile.objects.get(user=logged_user)
    
    print('hellooo.............',user)
    ctx={
        'user': user
    }
    return render(request, 'profile.html', ctx)





