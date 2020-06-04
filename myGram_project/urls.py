
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse_lazy

urlpatterns = [
    path('', include('myGram.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/',RegistrationView.as_view(success_url=reverse_lazy('my_profile')),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
   
    
    
]
