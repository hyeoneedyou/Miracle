from django.db import models
from django.contrib.auth.models import User

class Free(models.Model):
    name = models.CharField(max_length=10)
    goal_value = models.IntegerField(default=0)
    goal_unit = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    start_days = models.IntegerField(default=0)
    continuity_days = models.IntegerField(default=0)
    success_days = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Certify(models.Model):
    goal = models.ForeignKey(Free, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    fulfill_value = models.IntegerField(default=0)
    achievement = models.BooleanField(default=False)
