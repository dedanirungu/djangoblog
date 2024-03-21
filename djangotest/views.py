from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import  staff_member_required

from django.shortcuts import render

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
