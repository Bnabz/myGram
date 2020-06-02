
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostForm,ProfileForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    current_profile = Profile.objects.get(id = current_user.id)
    posts = Image.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', { "current_user":current_user, "current_profile":current_profile,"posts": posts ,"comments":comments})


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

@login_required(login_url='/accounts/login/')
def display_post(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = UserProfile.objects.get(id = current_user.id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return redirect("display_post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "display_post.html", {"post":post,"current_user":current_user,"current_profile":current_profile,"comment_form":comment_form,"comments":comments,})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    form = CommentForm()
    comments=Comment.objects.all()
  

    try:
        profile = Profile.objects.get(user=current_user)
        posts = Post.objects.filter(profile=current_user_id)
        title = profile.user
        username = profile.user
        post_number = len(posts)

    except ObjectDoesNotExist:
        return redirect('index')

    return render(request, 'profile.html',{"profile":profile,"posts":posts,"form":form,"post_number":post_number,"title":title,"username":username,"comments":comments})


def search_results(request):
    if 'searchterm' in request.GET and request.GET['searchterm']:
        search_term = request.GET.get("searchterm")
        searched_user = Profile.search_profile(search_term)
        posts = Image.objects.filter(profile__id=searched_user.id)
        message = f"{search_term}"

        return render(request,'search.html', {"message":message, "user":searched_user,"posts":posts})

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
                                                                        
                                                          
                                                          
                                                          