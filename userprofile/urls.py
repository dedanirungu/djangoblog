from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

urlpatterns = [
    #url(r'^register/$', views.register, name='user_register'),
    #path('fetch/', views.fetchInviterView, name='fetch_inviter'),
    #path('checkuser/', views.checkUserView, name='check_user_exist'),
]
