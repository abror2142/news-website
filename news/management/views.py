from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import PostForm
from posts.models import Post


User = get_user_model()


def is_writer(user):
    return user.groups.filter(name="writer").exists() or user.is_superuser

def is_mentor(user):
    return user.groups.filter(name="mentor").exists() or user.is_superuser


@login_required
@user_passes_test(is_writer)
def writer_posts(request):
    user = request.user
    posts = Post.objects.filter(writer=user)
    state = {
        "posts": posts
    }
    return render(request, "writer-posts.html", state)


@login_required
@user_passes_test(is_writer)
def writer_waiting_list(request):
    user = request.user
    posts = Post.objects.filter(writer=user)
    state = {
        "posts": posts
    }
    return render(request, "writer-waiting-list.html", state)


@login_required
@user_passes_test(is_writer)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return HttpResponse("Saved!")
    state = {
        "form": PostForm()
    }
    return render(request, "create-post.html", state)

