from django.db import models
from django.db import models


class Post(models.Model):
    Name= models.CharField(max_length=300, unique=True)
    Bike= models.TextField()
    