from django.db import models

# Create your models here.

class Session(models.Model):
    topic = models.CharField(max_length=255)

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=255)
    session = models.ForeignKey(Session)
    cached_text = models.CharField(max_length=200)
    username = models.CharField(max_length=255)

class Link(models.Model):
    url = models.TextField()
    session = models.ForeignKey(Session)
    
