from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index', permanent=False)), 
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
        # Define a URL for your index page (home)
]

