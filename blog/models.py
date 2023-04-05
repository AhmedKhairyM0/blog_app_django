from django.db import models
from django.urls import reverse # new
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.body[:30]
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk])
    