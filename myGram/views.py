
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostForm,ProfileForm
from django.contrib.auth.models import User
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    return render(request, 'index.html', {"posts": posts,})


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

        return redirect('index')

    else:
        form = PostForm()

    return render(request, 'create_post.html',{"form":form,"current_profile":current_profile })

@login_required(login_url='/accounts/login/')
def display_post(request, id):
    post = Image.objects.get(id = id)
    comments = Comment.objects.filter(image__id=id)
    current_user = request.user
    current_profile = Profile.objects.get(id = current_user.id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = current_user
            comment.image = post
            comment.save()
            comment_form = CommentForm()
            return redirect("display_post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "display_post.html", {"post":post,"current_user":current_user,"current_profile":current_profile,"comment_form":comment_form,"comments":comments,})

@login_required(login_url='/accounts/login/')
def profile(request,id):

    user = User.objects.get(id=id)
    profile = Profile.objects.get(id=id)
    posts = Image.objects.filter(profile__id=id)
    username = profile.user.username
    post_number = len(posts)
    
  

    return render(request, 'profile.html',{"profile":profile,"posts":posts,"user":user,"username":username,"post_number":post_number})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    id=request.user.id 
    profile = Profile.objects.get(id=id)
    posts = Image.objects.filter(profile__id=id)
    username = profile.user.username
    post_number = len(posts)
    

    return render(request, 'my_profile.html',{"profile":profile,"posts":posts,"current_user":current_user,"username":username,"post_number":post_number})
    


def search_results(request):
    # if 'searchterm' in request.GET and request.GET['searchterm']:
    #     search_term = request.GET.get("searchterm")
    #     # user = Profile.search_profile(search_term)
    #     user = User.objects.get(username = search_term)
    #     posts = Image.objects.filter(profile__id=user.id)
    #     message = f"{search_term}"

    #     return render(request,'search.html', {"message":message, "user":user,"posts":posts})

    # current_user = request.user
    # current_user_id=request.user.id
    # posts = Image.objects.filter(user=current_user_id)
    if 'searchterm' in request.GET and request.GET['searchterm']:
        search_term = request.GET.get("searchterm")
        searched_name = Profile.search_profile(search_term)
        print(searched_name)
      
        return render(request,'search.html', { "users":searched_name,})

    else:
        message = "You haven't searched for any username"
        return render(request,'search.html',{"message":message})


def like(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("index"))

def like_post(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return redirect("display_post", post.id)

@login_required(login_url='/accounts/login')
def edit_profile(request):

    form=ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')

        else:
            form=ProfileForm()

    return render(request,'edit_profile.html', {"form":form})
                                                                        
                                                          
                                                          
                                                          