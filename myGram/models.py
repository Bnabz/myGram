from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60,blank=True)
    caption = models.CharField(max_length =240,blank=True)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, caption_update):
        self.caption = caption_update
        self.save()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    bio =  models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300, blank=True)




