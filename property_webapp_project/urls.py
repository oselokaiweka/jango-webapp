"""
URL configuration for property_webapp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from users import views as user_views

# Temp! Dev Env Only!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class CustomLogoutView(auth_views.LogoutView):
    # Override to allow GET requests for logout
    http_method_names = ['get']
# Temp! Dev Env Only!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("realynx.urls")),
    path("signup/", user_views.signup, name="users-signup"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="auth-login"),
    path("logout/", CustomLogoutView.as_view(template_name="users/logout.html"), name="auth-logout"), # For dev environment only!  
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="auth-logout"),
]
