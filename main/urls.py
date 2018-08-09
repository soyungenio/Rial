"""rial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from main import views
from menu import views as pages
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^send_mail/', views.send_mail, name='send_mail'),
    url(r'^politica/', views.politica, name='politica'),
    url(r'^thankpage/', views.thankpage, name='thankpage'),
    url(r'^sitemap/', views.sitemap, name='sitemap'),
    url(r'^pricelist/(?P<price>\w+)/$', views.fork, name='fork'),
    url(r'^pricelist/', views.pricelist, name='pricelist'),
    url(r'^calculate/', views.calculate, name='calculate'),
    url(r'^replies/(?P<reply>\w+)/$', views.reply, name='reply'),
    url(r'^replies/', views.replies, name='replies'),
    url(r'^project/all', views.all_projects, name='all_projects'), 
    url(r'^vidy_rabot/', views.vidyrabot, name='vidyrabot'),
    #url(r'^type/(?P<type>\w+)$', views.type, name='type'),
    url(r'^(?P<category>\w+)/(?P<subcategory>\w+)/(?P<service>\w+)$', views.service, name='service'),
    url(r'^(?P<category>\w+)/(?P<subcategory>\w+)$', pages.page2, name='subcategory'),
    url(r'^(?P<category>\w+)/$', pages.page, name='category'),
    url(r'^project/(?P<project>\w+)/$', views.project, name='project')
]
