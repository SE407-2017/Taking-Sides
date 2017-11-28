from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    voted_questions = models.CharField(max_length=500, blank=True)
    liked_questions = models.CharField(max_length=500,blank=True)
    class Meta(AbstractUser.Meta):
        pass
