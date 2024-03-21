from .models import Blog,Category
import django_filters


"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""
class ManageBlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ['title', 'published', ]


class ManageBlogCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['title', ]



"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""

class UserBlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ['title', 'published',]

class UserBlogCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['title', ]




"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""