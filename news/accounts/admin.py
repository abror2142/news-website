from django.contrib import admin

from .models import User, UserInfo


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name']
    list_display_links = ['user']