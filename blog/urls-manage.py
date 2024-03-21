from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

"""TODO: add all the links"""
urlpatterns = [
    
    path('', views.ManageBlogView.as_view(), name='manage_blog_list'),
    path('create/', views.ManageBlogCreate.as_view(), name='manage_blog_create'),
    path('<int:pk>/update/', views.ManageBlogUpdate.as_view(), name='manage_blog_update'),
    path('<int:pk>/delete/', views.ManageBlogDelete.as_view(), name='manage_blog_delete'),

    path('category', views.ManageBlogCategoryView.as_view(), name='manage_blog_category_list'),
    path('category/create/', views.ManageBlogCategoryCreate.as_view(), name='manage_blog_category_create'),
    path('category/<int:pk>/update/', views.ManageBlogCategoryUpdate.as_view(), name='manage_blog_category_update'),
    path('category/<int:pk>/delete/', views.ManageBlogCategoryDelete.as_view(), name='manage_blog_category_delete'),



]

