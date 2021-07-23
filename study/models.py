from django.db import models
from django.contrib.auth.models import User


class Study(models.Model):
    name = models.CharField(max_length=10)
    goal_hour = models.IntegerField(default=0)
    goal_minute = models.IntegerField(default=0)
    created = models.DateField()
    start_days = models.IntegerField(default=0)
    continuity_days = models.IntegerField(default=0)
    success_days = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Certify(models.Model):
    goal = models.ForeignKey(Study, on_delete=models.CASCADE, related_name='certifies')
    created = models.DateField()
    fulfill_hour = models.IntegerField(default=0)
    fulfill_minute = models.IntegerField(default=0)
    achievement = models.BooleanField(default=False)
