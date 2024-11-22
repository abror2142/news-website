from django.contrib import admin
from .models import Category, Post, PostCategory
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['id', 'name']
    list_display_links = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['id', 'title']
    list_display_links = ['title']


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display= ['id', 'category', 'post']
    list_display_links = ['category', 'post']