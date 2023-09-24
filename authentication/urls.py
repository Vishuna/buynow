from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns=[
  path('',views.register,name="register"),
  path('login/',views.login,name="login"),
  path('check_username/', views.check_username, name='check_username'),

  path('menu/',views.sidebar_menu,name='sidebar_menu'),
  # add group
  path('add_group/',views.add_group,name="add_group"),

  # home
  path('home/',views.home,name="home"),
  
]