from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/',views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('like/', views.like, name="like"),
    
]