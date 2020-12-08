#users/urls.py
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index),
    path('view_product/<pk>',viewProduct),
    path('order_product/<pk>',orderProduct),
    path('thank_you',thankYou),
    path('contact',Contact),
]