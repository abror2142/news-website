from django.shortcuts import render

# Create your views here.
from .forms import PostForm


def create_post(request):
    state = {
        "form": PostForm()
    }
    return render(request, "create-post.html", state)

