from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost

import uuid

# Create your views here.


@login_required(login_url='index')
def feed_view(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts': posts})

@login_required(login_url='index')
def upload(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        caption = request.POST['caption']

        #media check
        if not image and not video:
            messages.info(request, 'Upload Failed')
            return redirect('feed')

        new_post = Post.objects.create(user=user, image=image, video=video, caption=caption)
        new_post.save()
    else:
        messages.info(request, 'Upload Failed')
        return redirect('feed')

    
    return render(request, 'feed.html')

@login_required(login_url='index')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')
