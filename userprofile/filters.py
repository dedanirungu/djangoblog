from django.contrib.auth.models import User, Group
import django_filters


"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""


class ManageUserprofileUserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile__gender', 'profile__phone', 'is_active']


class ManageUserprofileGroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = ['name', ]




"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""
