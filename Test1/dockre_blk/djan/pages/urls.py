# pages/urls.py
from django.urls import path

from .views import homePageView
from .views import post_new

urlpatterns = [
    path('1/', homePageView, name='home'),
    path('',post_new, name='post_new'),
]
