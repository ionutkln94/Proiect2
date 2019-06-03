"""Livrador2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from django.conf.urls import url
from Web import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),

    re_path(r'^supermarket/sign-in/', auth_views.LoginView.as_view(template_name='supermarket/sign-in.html'), name='supermarket_sign_in'),
    re_path(r'^supermarket/sign-out/', auth_views.LogoutView.as_view(template_name='/'), name='supermarket_sign_out'),

    re_path(r'^supermarket/sign-up/', views.supermarket_sign_up, name='supermarket_sign_up'),

    re_path(r'^supermarket/$', views.supermarket_home, name = 'supermarket_home')
]
