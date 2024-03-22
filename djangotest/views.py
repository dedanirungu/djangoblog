from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import  staff_member_required

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



@staff_member_required
@login_required
def manage_dashboard(request):
    """View function for dashboard of site."""
    context = {
        'title': "Manage Dashboard",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/dashboard.html', context=context)

@staff_member_required
@login_required
def manage_users_list(request):
    """View function for dashboard of site."""
    context = {
        'title': "Manage Users",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/users.html', context=context)

@staff_member_required
@login_required
def manage_users_groups_list(request):
    """View function for dashboard of site."""
    context = {
        'title': "Manage Users",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/users_groups.html', context=context)

@staff_member_required
@login_required
def manage_users_permissions_list(request):
    """View function for dashboard of site."""
    context = {
        'title': "Manage Users",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/users_permissions.html', context=context)

@staff_member_required
@login_required
def manage_dashboard(request):
    """View function for dashboard of site."""
    context = {
        'title': "Manage Dashboard",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/dashboard.html', context=context)    


@staff_member_required
@login_required
def profile(request):
    """View function for dashboard of site."""
    context = {
        'title': "User Profile",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'manage/profile.html', context=context)
    
def homepage(request):
    """View function for dashboard of site."""
    context = {
        'title': "Top Blog Test App",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'front/homepage.html', context=context)

def resetSearch(request):

    next_to = request.GET.get('next_to')

    if  request.session.has_key('query_data'):
        query_data = request.session['query_data']  
        
        if next_to in query_data:
            del query_data[next_to]

    return redirect(next_to)

