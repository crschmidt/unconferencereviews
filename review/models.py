from django.db import models

# Create your models here.

class Session(models.Model):
    topic = models.TextField(max_length=255)

