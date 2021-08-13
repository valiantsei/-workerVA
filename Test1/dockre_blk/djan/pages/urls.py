# pages/urls.py
from django.urls import path

from .views import homePageView
from .views import post_new

urlpatterns = [
    path('', homePageView, name='home'),
    path('1/',post_new, name='post_new'),
]
