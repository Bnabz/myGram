from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<id>/',views.profile, name='profile'),
    path('my_profile/',views.my_profile, name='my_profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('display_post/<id>', views.create_post, name='display_post'),
    path('like/<id>', views.like, name="like"),
    path('like_post/<id>', views.like, name="like_post"),
    path('search/',views.search_results, name='search'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)