from .tables import ManageBlogCategoryTable
from .filters import ManageBlogCategoryFilter
from .models import Category

from .tables import ManageBlogTable
from .filters import ManageBlogFilter
from .models import Blog

from .tables import UserBlogTable
from .filters import UserBlogFilter

from .tables import UserBlogCategoryTable
from .filters import UserBlogCategoryFilter

from django.shortcuts import render
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    """View function for blog page of site."""

    context = {
        'title': "Blogs",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Blog
    table_class = ManageBlogTable
    template_name = 'manage/blog_blog_list.html'

    filterset_class = ManageBlogFilter

    permission_required = 'blog.view_blog'  
    
    paginate_by = 20

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['limit'] = int(self.request.GET.get('limit',20))

        return context

    def get_paginate_by(self, queryset):

        limit = self.request.GET.get('limit')

        self.paginate_by = limit if limit else self.paginate_by

        return self.paginate_by

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogCreate(PermissionRequiredMixin, CreateView):
    template_name = 'manage/blog_blog_form.html'
    model = Blog
    fields = ['category', 'business', 'title', 'slug', 'price', 'price', 'featured_image',
              'description', 'discount', 'location', 'expiry_date', 'hits', 'published',
              ]
    permission_required = 'blog.add_blog'

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'manage/blog_blog_form.html'
    model = Blog
    fields = ['category', 'business', 'title', 'slug', 'price', 'price', 'featured_image',
              'description', 'discount', 'location', 'expiry_date', 'hits', 'published',
              ]

    permission_required = 'blog.change_blog'

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'manage/blog_blog_confirm_delete.html'
    model = Blog
    success_url = reverse_lazy('manage_blog_list')
    permission_required = 'blog.delete_blog'


"""------------------- Category ---------------------- """

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogCategoryView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Category
    table_class = ManageBlogCategoryTable
    template_name = 'manage/blog_category_list.html'

    filterset_class = ManageBlogCategoryFilter

    permission_required = 'blog.view_category'

    paginate_by = 20

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['limit'] = int(self.request.GET.get('limit',20))

        return context

    def get_paginate_by(self, queryset):

        limit = self.request.GET.get('limit')

        self.paginate_by = limit if limit else self.paginate_by

        return self.paginate_by

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogCategoryCreate(PermissionRequiredMixin, CreateView):
    template_name = 'manage/blog_category_form.html'
    model = Category
    fields = ['title', 'description', 'published', ]
    permission_required = 'blog.add_category'

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogCategoryUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'manage/blog_category_form.html'
    model = Category
    fields = ['title', 'description', 'published', ]

    permission_required = 'blog.change_category'

@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageBlogCategoryDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'manage/blog_category_confirm_delete.html'
    model = Category
    success_url = reverse_lazy('manage_blog_category_list')
    permission_required = 'blog.delete_category'


"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""


class UserBlogView( SingleTableMixin, FilterView):
    model = Blog
    table_class = UserBlogTable
    template_name = 'user/blog_blog_list.html'

    filterset_class = UserBlogFilter

    permission_required = 'blog.view_blog'


class UserBlogCreate(CreateView):
    template_name = 'user/blog_blog_form.html'
    model = Blog
    fields = ['category', 'business', 'title', 'slug', 'price', 'price', 'featured_image',
              'description', 'discount', 'location', 'expiry_date', 'hits', 'published',
              ]
    permission_required = 'blog.add_blog'


class UserBlogUpdate(UpdateView):
    template_name = 'user/blog_blog_form.html'
    model = Blog
    fields = ['category', 'business', 'title', 'slug', 'price', 'price', 'featured_image',
              'description', 'discount', 'location', 'expiry_date', 'hits', 'published',
              ]

    permission_required = 'blog.change_blog'


class UserBlogDelete(DeleteView):
    template_name = 'user/blog_blog_confirm_delete.html'
    model = Blog
    success_url = reverse_lazy('user_blog_list')
    permission_required = 'blog.delete_blog'


"""------------------- Category ---------------------- """


class UserBlogCategoryView( SingleTableMixin, FilterView):
    model = Category
    table_class = UserBlogCategoryTable
    template_name = 'user/blog_category_list.html'

    filterset_class = UserBlogCategoryFilter

    permission_required = 'blog.view_category'

"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""
