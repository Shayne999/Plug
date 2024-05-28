from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post

def feed_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    for post in posts:
        context[f'post_{post.id}_id'] = post.id
    return render(request, 'feed.html', context)

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

def like_post(request, post_id):
    username = request.user.username
    #post_id = request.GET.get('post_id')

    post = Post.object.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.like_count += 1
        post.save()
        return redirect('feed')
    else:
        like_filter.delete()
        post.like_count -= 1
        post.save()
        return redirect('feed')

