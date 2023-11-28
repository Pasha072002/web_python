from django.urls import re_path as url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]