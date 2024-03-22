"""
URL configuration for djangotest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('tinymce/', include('tinymce.urls')),
]

from django.contrib.auth import views as auth_views


urlpatterns += [
    # Other URL patterns...
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # Other URL patterns...
]

urlpatterns += [
    # Other URL patterns...

    path('', views.homepage, name='index'),
    path('', views.homepage, name='home'),
    path('manage/', views.manage_dashboard, name='manage_dashboard'),
    path('manage/profile/', views.profile, name='manage-profile'),
    path('accounts/profile/', views.profile, name='accounts-profile'),

    path('resetsearch/', views.resetSearch, name='reset_search'),

    #path('common/', include('common.urls')),

    path('manage/users/', views.manage_users_list, name='manage_users_list'),
    path('manage/groups/', views.manage_users_groups_list, name='manage_users_groups_list'),
    path('manage/permissions/', views.manage_users_permissions_list, name='manage_users_permissions_list'),

    path('blog/', include('blog.urls')),
    path('user/blog/', include('blog.urls-user')),
    path('manage/blog/', include('blog.urls-manage')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'common.views.handler404'
handler500 = 'common.views.handler500'

