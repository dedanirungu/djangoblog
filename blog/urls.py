from django.urls import path
from . import views

"""TODO: add all the links"""
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('', views.index, name='user-blog-index'),
]

