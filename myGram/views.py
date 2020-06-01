
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostForm,ProfileForm
from django.contrib.auth.models import User

 @login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    current_profile = UserProfile.objects.get(id = current_user.id)
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    form = CommentForm()
    comments = Comment.objects.all()
    
    return render(request, 'index.html', { "current_user":current_user, "current_profile":current_profile,"posts": posts ,"profiles":profiles,"form":form, "comments":comments})


@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    current_profile = Profile.objects.filter(user=current_user)


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.likes = 0
            post.save()

        return redirect('home')

    else:
        form = PostForm()

    return render(request, 'create_post.html',{"form":form,"current_profile":current_profile })