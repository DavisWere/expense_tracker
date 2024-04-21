from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'home.html')