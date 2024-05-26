from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('home')
        else:
           messages.info(request, 'Invalid Credentials')
           return redirect('index')

    else:
        return render(request, 'index.html')
    return render(request, 'index.html')

# def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('home')
        else:
           messages.info(request, 'Invalid Credentials')
           return redirect('index')

    else:
        return render(request, 'index.html')
    
def sign_up(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
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
                #user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                #finish the profile
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)
            
                #profile object for new user
                user_models = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_models, id_user=user_models.id)
                new_profile.save()
                return redirect('home')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('sign_up')
    else:
        return render(request, 'sign_up.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='index')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='index')
def home(request):
    users = Profile.objects.all()
    return render(request, 'home.html', {'users':users})

@login_required(login_url='index')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
            bio = request.POST['bio']
            location = request.POST['location']
            username = request.POST['username']
            email = request.POST['email']

            if 'profileimg' in request.FILES:
                profileimg = request.FILES['profileimg']
            else:
                profileimg = user_profile.profileimg

            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.username = username
            user_profile.email = email
            user_profile.save()

            return redirect('settings')
    return render(request, 'settings.html', {'user_profile':user_profile})

@login_required(login_url='index')
def chat(request):
    return render(request, 'chat.html')

@login_required(login_url='index')
def connections(request):
    return render(request, 'connections.html')