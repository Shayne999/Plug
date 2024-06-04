from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost, Favorite
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.urls import reverse

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
        #new_post.save()
        return redirect('feed')
    else:
        messages.info(request, 'Upload Failed')
        return redirect('feed')
    #return render(request, 'feed.html')

@login_required(login_url='index')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')


@login_required(login_url='index')
def favorite_posts(request):
    user_favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorite_posts.html', {'favorites': user_favorites})

def add_to_favorites(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    profile = request.user.profile
    profile.favorites.add(post)
    return redirect('feed')
    
@login_required(login_url='index')
def favorites_view(request):
    profile = request.user.profile
    favorites = profile.favorites.all()
    return render(request, 'favorites.html', {'favorites': favorites})


@login_required(login_url='index')
def remove_from_favorites(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    profile = request.user.profile
    profile.favorites.remove(post)
    return redirect('feed')


@login_required(login_url='index')
def upload_page(request):
    return render(request, 'upload.html')


class DeletePostView(DeleteView):
    model = Post

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('post_id')
        return Post.objects.get(id=uuid)

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('profilepage', kwargs={'username': username})