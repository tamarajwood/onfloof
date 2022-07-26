"""onfloof_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('adopt/', TemplateView.as_view(template_name='adopt.html'), name='adopt'),
    path('adopt/<int:pk>', TemplateView.as_view(template_name='dog-detail.html'), name='dog-detail'),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('<int:pk>/', TemplateView.as_view(template_name='post.html'), name='post'),
    path('bike/', TemplateView.as_view(template_name='bike.html'), name='bike'),
    path('hike/', TemplateView.as_view(template_name='hike.html'), name='hike'),
    path('mushing/', TemplateView.as_view(template_name='mush.html'), name='mush'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
