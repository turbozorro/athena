from django.shortcuts import render

# Create your views here.
def startup(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')