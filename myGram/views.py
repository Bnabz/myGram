
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostForm,ProfileForm
from django.contrib.auth.models import User

# @login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    current_profile = UserProfile.objects.get(id = current_user.id)
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    form = CommentForm()
    comments = Comment.objects.all()
    
    return render(request, 'index.html', { "current_user":current_user, "current_profile":current_profile,"posts": posts ,"profiles":profiles,"form":form, "comments":comments})

    
