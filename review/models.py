from django.db import models

# Create your models here.

class Session(models.Model):
    topic = models.CharField(max_length=255)

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=255)
    session = models.ForeignKey(Session)

class Link(models.Model):
    url = models.TextField()
    session = models.ForeignKey(Session)
    
