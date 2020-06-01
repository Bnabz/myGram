from django import forms
from .models import Image,Comment,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=['profile','date_uploaded','likes',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'image']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }


