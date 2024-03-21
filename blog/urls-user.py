from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

"""TODO: add all the links"""
urlpatterns = [
    path('', views.UserBlogView.as_view(), name='user_blog_list'),
    path('create/', views.UserBlogCreate.as_view(), name='user_blog_create'),
    path('<int:pk>/update/', views.UserBlogUpdate.as_view(), name='user_blog_update'),
    path('<int:pk>/delete/', views.UserBlogDelete.as_view(), name='user_blog_delete'),

    path('category', views.UserBlogCategoryView.as_view(), name='user_blog_category_list'),

]

