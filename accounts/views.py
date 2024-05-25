from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('home.html')
        else:
           messages.info(request, 'Invalid Credentials')
           #return redirect('/')

    else:
        return render(request, 'index.html')
    
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('sign_up')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('sign_up')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
            
                #profile object for new user
                user_models = User.object.get(username=username)
                new_profile = Profile.objects.create(user=user_models, id_user=user_models.id)
                new_profile.save()
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('sign_up')
    else:
        return render(request, 'sign_up.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html')
