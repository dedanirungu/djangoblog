from django.conf.urls import url
from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^register/$', views.register, name='user_register'),
    path('fetch/', views.fetchInviterView, name='fetch_inviter'),
    path('checkuser/', views.checkUserView, name='check_user_exist'),
    path('email_verification/', views.emailVerificationView, name='email_verification'),
    path('thankyou/', views.registerThankView, name='register_thank'),
    path('location/api/', views.locationApi, name='location_api'),

    
]
