from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60,blank=True)
    caption = models.CharField(max_length =240,blank=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    likes = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)


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
     
    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender = User)
    def create_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile( sender, instance, **kwargs):
        instance.profile.save()

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300, blank=True)

    def __str__(self):
        return self.comment

    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()




