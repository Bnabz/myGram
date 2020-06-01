from django import forms
from .models import Image,Comment,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=['profile','date_uploaded','likes']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['followers','following']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'image']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }


