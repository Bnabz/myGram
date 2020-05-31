from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =240)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    bio =  models.TextField(blank=True)

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300, blank=True)




