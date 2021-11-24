from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.urls import reverse,reverse_lazy
# Create your models here.


class Members(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    #name=models.CharField(max_length=200)
    username_for_site=models.CharField(max_length=256)
    block=models.PositiveIntegerField()
    flat_number=models.CharField(max_length=200)
    intercom_number=models.PositiveIntegerField()

    last_played = models.DateTimeField(default=timezone.now)

    def last_played_time(self):
       self.last_played=timezone.now()
    def __str__(self):
        return self.username.username


class Scores(models.Model):
    score=models.PositiveIntegerField()
    name=models.ForeignKey(Members,on_delete=models.CASCADE)

class Post(models.Model):
    Username=models.ForeignKey(User,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='media')
    Title=models.CharField(max_length=256)
    title_slug=models.SlugField(default='hi')
    Description=models.TextField()

    def save(self,*args,**kwargs):

        self.title_slug=slugify(self.Title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("index")


class post_comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user_commented=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_commented')
    comment=models.TextField()
    def get_absolute_url(self):
        return  reverse('insidepage')
# class Music(models.Model):
#     user_uploaded = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music')
#     Song_Name=models.CharField(max_length=256)
#
#     Genre=models.CharField(max_length=95)
#     Song_File=models.FileField()
#     Cover_Picture=models.ImageField(blank=True,upload_to='media')
#     Description=models.TextField(blank=True)
#
#     def get_absolute_url(self):
#         return reverse('music')
class MusicCreate(models.Model):
    Song_Name = models.CharField(max_length=256)
    user_uploaded = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music')
    Artist_Name = models.CharField(max_length=256)
    Genre = models.CharField(max_length=95)
    Song_File = models.FileField()
    Cover_Picture = models.ImageField(blank=True, upload_to='media')
    Description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('music')
    def __str__(self):
        return self.Song_Name