from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def startup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')

@login_required
def home(request):
    user_subjects = UserSubject.objects.filter(user=request.user)
    context = {
        'user_subjects': user_subjects,
    }
    return render(request, 'home.html', context)