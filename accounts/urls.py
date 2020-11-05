#accounts/urls.py
from django.urls import include,path
from .views import *
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('signup',signup),
]
