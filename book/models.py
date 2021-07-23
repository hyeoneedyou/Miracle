from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=10)
    goal_page = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    start_days = models.IntegerField(default=0)
    continuity_days = models.IntegerField(default=0)
    success_days = models.IntegerField(default=0)
    total_page = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Certify(models.Model):
    goal = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='certifies')
    created = models.DateField(auto_now=True)
    book_name = models.CharField(max_length=50)
    fulfill_page = models.IntegerField(default=0)
    achievement = models.BooleanField(default=False)
