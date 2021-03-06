"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Mysite import settings
import django.views.static
from BU.upload import upload_image
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve, {"document_root": settings.MEDIA_ROOT, }),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imgs/favicon.ico')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('BU.urls')),
]
