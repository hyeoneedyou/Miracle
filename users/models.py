from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    level = models.IntegerField(default=1)
