from django import forms
from .models import Image,Comment,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=['profile','date_uploaded','likes',]


