from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=126)
    content = models.TextField(max_length=1000)
    published_date = models.DateTimeField(auto_now_add=True)
