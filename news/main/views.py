from django.shortcuts import render
from posts.models import Category, PostCategory, Post


def home_view(request):
    state = {
        "categories": Category.objects.all(),

    }
    return render(request, "index.html", state)