from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from feed.models import Post

@login_required(login_url='index')
def profilepage(request, username):
    #returns the profile page with the user profile data
    user_object = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user_object)
    user_posts = Post.objects.filter(user=user_object)
    user_posts_length = user_posts.count()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_posts_length': user_posts_length,
    }
    return render(request, 'profile.html', context)