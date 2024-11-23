from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True)

    def __str__(self):
        return f"{self.user} -> {self.first_name} {self.last_name}"


