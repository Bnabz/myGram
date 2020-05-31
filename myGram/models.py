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
    caption = models.CharField(max_length =360)

# class Comment(models.Model):
#     poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
#     comment = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.comment

#     def save_comment(self):
#         self.save()

#     @classmethod
#     def get_comment(cls):
#         comment = Comment.objects.all()
#         return comment
