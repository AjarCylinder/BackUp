from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavni),
    path('/wishlist', views.base)
]
