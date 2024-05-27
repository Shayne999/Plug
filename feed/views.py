from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

def feed_view(request):

    #shows feed posts and profile image
    posts = Post.objects.select_related('user__profile').all()

    return render(request, 'feed.html', {'posts':posts})

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