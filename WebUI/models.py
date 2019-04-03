from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
import os


class Post(models.Model):
    """
    this model represent ORM for Each post user want to send in artige.ir
    """
    id = models.AutoField(primary_key=True)
    # artige_id = models.ManyToManyField(User)
    artige_id = models.IntegerField()
    title = models.CharField(max_length=12000)
    description = models.CharField(max_length=12000)
    tags = models.CharField(max_length=12000)
    images = models.CharField(max_length=12000)
    post_like = models.IntegerField(default=0)

    @property
    def array_tags(self):
        return self.tags.split(" ")

    @property
    def array_images(self):
        arr = self.images.split(" ")
        return arr

    def __str__(self):
        return self.title


class PostLike(models.Model):
    """
    Each Post Will Get Like In Final Project And Here we Can Find Out which user Like Which Post
    """
    id = models.AutoField(primary_key=True)
    liker = models.ManyToManyField(User)
    post = models.ManyToManyField(Post)
    media = models.CharField(max_length=1000)


class PostComment(models.Model):
    """
    each post will receive comment from other users and this model represent which user comment on which post
    """
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User)
    post = models.ManyToManyField(Post)
    comment = models.CharField(max_length=512)
