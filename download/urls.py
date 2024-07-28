from django.contrib import admin 
from django.urls import path 
from download import views
from django.views.static import serve 
#from yt_video import settings
urlpatterns = [
    path("",views.home,name="home"), 
    path("home",views.home,name="home"),
    path("index",views.index,name='index'),
    path("service", views.service,name="service"),
]
