"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from core import views 
from . import views as mainviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainviews.home, name='home'),
    path('add_snippet/', views.add_snippet, name='add_snippet'),
        path('saved_snippet/', views.saved_snippet, name='saved_snippet'),

        path('my_snippet/', views.my_snippet, name='my_snippet'),
        path('snippet/<int:id>/', views.snippet_detail, name='snippet_detail'),
        path('snippet/<int:id>/toggle-save/', views.toggle_save_snippet, name='toggle_save_snippet'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]


