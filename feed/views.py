from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

def feed_view(request):
    return render(request, 'feed.html')

def upload(request):
    return render(request, 'feed.html')