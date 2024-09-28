"""
URL configuration for bu_hacktoberfest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import profile, profile_view, welcome_view, leaderboard_view, update_all
from .views import home, login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name='profile'),
    # path('profile/pr/<int:id>/', pr_detail_view, name='pr_detail'),
    path('', home),
    path('login/', login),
    path('welcome/', welcome_view, name='welcome'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('update_all/', update_all, name='update_all'),    
]
