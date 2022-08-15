"""mysite URL Configuration

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
from mysite.views import *

from django.conf.urls.static import static
from django.conf import settings

from mysite.views import UserCreateView, UserCreateDoneTV
from printer3d.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^list/$', Printer3DLV.as_view(), name="list"),
    url(r'^list/(?P<pk>\d+)/$', Printer3DDV.as_view(), name="detail"),
    url(r'^add/$',Printer3D_CreateView.as_view(),name="add"),
    url(r'^(?P<pk>[0-9]+)/update/$', Printer3D_UpdateView.as_view(), name="update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', Printer3D_DeleteView.as_view(), name="delete"),

    url(r'^reservation/add/$', Reservation_CreateView.as_view(), name='reservation_add'),
    url(r'^reservation/list/$', Reservation_ListView.as_view(), name='reservation_list'),

    url(r'^(?P<pk>[0-9]+)/update_extra/$', Printer3D_UpdateExtraView.as_view(), name="update_extra"),

    url(r'^what/$', WhatView.as_view(), name='what'),
    url(r'^why/$', WhyView.as_view(), name='why'),
    url(r'^how/$', HowView.as_view(), name='how'),

    url(r'^review/$', ReviewView.as_view(), name='review'),







] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
