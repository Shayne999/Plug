from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from feed.models import Post

# Create your views here.
def index(request):
    #returns the index page with the latest posts and users
    
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
        latest_posts = Post.objects.all().order_by('-created_at')[:3]  # Get the latest 5 posts
        latest_profiles = Profile.objects.select_related('user').order_by('-user__date_joined')[:3]  # Get the latest 3 users
        return render(request, 'index.html', {'latest_posts': latest_posts, 'latest_profiles': latest_profiles})
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
    #returns the sign up page and uploads new user data on the database
    if request.method == 'POST':
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
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                # Authenticate and login
                user_login = auth.authenticate(username=username, password=password)
                if user_login is not None:
                    auth.login(request, user_login)
            
                    # No need to create profile here, signal handles it
                    return redirect('home')
                else:
                    messages.info(request, 'Authentication Failed')
                    return redirect('sign_up')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('sign_up')
    else:
        return render(request, 'sign_up.html')


def logout(request):
    #logs out the user and takes them to the login page(index page)
    auth.logout(request)
    return redirect('/')

@login_required(login_url='index')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='index')
def home(request):
    #returns the home page with all the available users excluding the currently logged in user
    users = Profile.objects.exclude(user=request.user)
    return render(request, 'home.html', {'users':users})



@login_required(login_url='index')
def settings(request):
    #returns the settings page with the user profile data and allows the user to edit the data
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
            bio = request.POST['bio']
            location = request.POST['location']
            username = request.POST['username']
            email = request.POST['email']
            genre = request.POST['genre']

            if 'profileimg' in request.FILES:
                profileimg = request.FILES['profileimg']
            else:
                profileimg = user_profile.profileimg

            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.username = username
            user_profile.email = email
            user_profile.genre = genre
            user_profile.save()

            return redirect('settings')
    return render(request, 'settings.html', {'user_profile':user_profile})


@login_required
def delete_profile_view(request):
    #deletes the user profile
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('index')
    return render(request, 'settings.html')