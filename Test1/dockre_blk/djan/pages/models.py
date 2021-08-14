from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=18)
    def __str__(self):
        return self.title
