from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request, 'index.html')
