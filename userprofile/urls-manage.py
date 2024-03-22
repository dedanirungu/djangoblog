from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

"""TODO: add all the links"""
urlpatterns = [

    path('activate_user/', views.manage_activate_user, name='manage_activate_user'),
    path('create_user/', views.manage_create_user, name='manage_create_user'),
    path('generate_user/', views.manage_generate_user, name='manage_generate_user'),
    path('change_user_groups/', views.manage_change_user_groups, name='manage_change_user_groups'),
    path('change_group_permissions/', views.manage_change_group_permissions, name='manage_change_group_permissions'),
    path('change_password/', views.manage_change_password, name='manage_change_password'),

    path('', views.ManageUserprofileUserView.as_view(), name='manage_userprofile_user_list'),
    path('create/', views.ManageUserprofileUserCreate.as_view(), name='manage_userprofile_user_create'),
    path('<int:pk>/update/', views.ManageUserprofileUserUpdate.as_view(), name='manage_userprofile_user_update'),
    path('profile/<int:pk>/update/', views.ManageUserprofileProfileUpdate.as_view(), name='manage_userprofile_profile_update'),
    path('<int:pk>/delete/', views.ManageUserprofileUserDelete.as_view(), name='manage_userprofile_user_delete'),

    path('group/', views.ManageUserprofileGroupView.as_view(), name='manage_userprofile_group_list'),
    path('group/create/', views.ManageUserprofileGroupCreate.as_view(), name='manage_userprofile_group_create'),
    path('group/<int:pk>/update/', views.ManageUserprofileGroupUpdate.as_view(), name='manage_userprofile_group_update'),
    path('group/<int:pk>/delete/', views.ManageUserprofileGroupDelete.as_view(), name='manage_userprofile_group_delete'),

]

