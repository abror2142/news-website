from django.db import models

from tinymce.models import HTMLField

from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    content = HTMLField()
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title 
  

class PostReview(models.Model):

    REVIEW_STATUS_CHOICES = {
        "ACC": "Accepted",
        "REV": "Review Required",
        "DEC": "Declined",
        "SENT": "Sent to review"
    }

    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feedback = models.TextField()
    status = models.CharField(max_length=4, choices=REVIEW_STATUS_CHOICES)

    def __str__(self):
        return f"{self.post} {self.mentor}"


class PostCategory(models.Model):
    """One post may be related to many categories and vice verca."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.post} -> {self.post}"