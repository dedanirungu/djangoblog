from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import  staff_member_required

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from blog.models import Blog, Category



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

    top_one = Blog.objects.all().order_by('-created_at')[:1]
    top_two = Blog.objects.all().order_by('-created_at')[:2]
    top_three = Blog.objects.all().order_by('-created_at')[:3]
    most_recent = Blog.objects.all().order_by('-created_at')[:5]
    most_popular = Blog.objects.all().order_by('-hits')[:5]
    categories = Category.objects.all()

    context = {
        'title': "Top Blog Test App",
        'most_recent': most_recent,
        'most_popular': most_popular,
        'top_three': top_three,
        'top_two': top_two,
        'top_one': top_one,
        'categories': categories
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'front/homepage.html', context=context)

def about(request):
    """View function for dashboard of site."""
    context = {
        'title': "About Top Blog Test App",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'front/about.html', context=context)

def blog(request, id):
    """View function for blog page of site."""

    blog = Blog.objects.get(id=id)

    context = {
        'title': "Blogs",
        'blog': blog,
    }

    # Render the HTML template blog.html with the data in the context variable
    return render(request, 'front/blog.html', context=context)


def blogs(request):
    """View function for dashboard of site."""

    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)

    offset = int(page) * int(limit) - int(limit)

    """ Genereate a list of most blogs with implemented pagination """
    blogs = Blog.objects.all().order_by('-created_at').all()[int(offset):int(limit)]
    categories = Category.objects.all()
    most_popular = Blog.objects.all().order_by('-hits')[:5]

    # count blogs for each category and save count in blog_count
    for category in categories:
        category.blog_count = Blog.objects.filter(category=category).count()


    context = {
        'title': "Top Blog Test App",
        'blogs': blogs,
        'categories': categories,
        'most_popular': most_popular,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'front/blogs.html', context=context)

def contact(request):
    """View function for dashboard of site."""
    context = {
        'title': "Contact Top Blog Test App",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'front/contact.html', context=context)
    


def resetSearch(request):

    next_to = request.GET.get('next_to')

    if  request.session.has_key('query_data'):
        query_data = request.session['query_data']  
        
        if next_to in query_data:
            del query_data[next_to]

    return redirect(next_to)

