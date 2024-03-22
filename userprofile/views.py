from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import redirect, render, get_object_or_404
from django.db import models
from django.contrib import messages

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.http import JsonResponse

from setup.models import Country, Location
from .models import Profile
from .forms import UserForm, ProfileForm, ManageUserForm
from .tokens import account_activation_token
from affiliate.models import Agreement

from django.utils.dateparse import parse_date
from datetime import datetime

from newsletter.classes.Mailer import Mailer

from dynamic_preferences.registries import global_preferences_registry

from .tables import ManageUserprofileGroupTable
from .filters import ManageUserprofileGroupFilter

from .tables import ManageUserprofileUserTable
from .filters import ManageUserprofileUserFilter

from django.shortcuts import render
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.conf import settings

from common.middleware import RequestMiddleware

from common.classes.Common import Common
from django import forms

import json
import random
import re


def register(request):

    inviter_id = 0
    error_message = ''
    has_error = False
    registered = False

    mailer = Mailer()
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        username = request.POST.get('username')
        email = request.POST.get('email')
        inviter_id = request.POST.get('inviter_id')
        country_id = request.POST.get('country_id')

        code = random.randint(100000, 999999)

        existing_username = User.objects.filter(username=username).all()
        existing_email = User.objects.filter(email=email).all()

        if existing_username:
            error_message = error_message + ' Username is Aready Taken.'
            has_error = True

        if existing_email:
            error_message = error_message + ' Email is Aready Taken.'
            has_error = True

        if not has_error and user_form.is_valid() and profile_form.is_valid():

            user_data = user_form.cleaned_data
            profile_data = profile_form.cleaned_data

            global_preferences = global_preferences_registry.manager()
            email_verification = global_preferences['userprofile__email_verification']
            verification_by_code = global_preferences['userprofile__verification_by_code']

            user = User.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
                is_active=False if email_verification else True,
            )

            for_inviter = User.objects.get(id=1)
            try:
                for_inviter = User.objects.get(id=inviter_id)
            except:
                pass

            Profile.objects.create(
                user=user,
                country=Country.objects.filter(id=country_id).first(),
                inviter=for_inviter,
                code=code,
                gender=int(profile_data['gender']),
                date_of_birth=profile_data['date_of_birth'],
                address=profile_data['address'],
                phone=profile_data['phone'],
                town=profile_data['town'],
                location=profile_data['town']
            ).save()

            group, created = Group.objects.get_or_create(name='Registered')
            if group:
                user.groups.add(group)

            if email_verification:
                domain = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)

                email_verification_link = 'http://' + \
                    str(domain) + '/user/email_verification/' + \
                    '?uidb64=' + str(uid) + '&token=' + str(token)

                request.session['code'] = code
                request.session['registered_email'] = user.email

                email_context = {
                    'user': user,
                    'to': user.email,
                    'domain': domain,
                    'uid': uid,
                    'token': token,
                    'code': code,
                    'email_verification_link': email_verification_link,
                }

                if verification_by_code:
                    mailer.sendTemplateMail(
                        'user.email.verification.by.code', email_context)
                else:
                    mailer.sendTemplateMail(
                        'user.email.verification', email_context)

            registered = True

            return redirect('register_thank')
        else:
            error_message = error_message + \
                ' '.join([' '.join(x for x in l)
                          for l in list(user_form.errors.values())])
            error_message = error_message + \
                ' '.join([' '.join(x for x in l)
                          for l in list(profile_form.errors.values())])
            has_error = True

    inviter = None

    if 'inviter' in request.session:
        try:
            inviter = User.objects.get(username=request.session['inviter'])
        except:
            pass
    # else:
    #    inviter = User.objects.get(id=1)

    if inviter_id:
        inviter = User.objects.get(id=inviter_id)

    agreements = Agreement.objects.filter(target='registration').all()

    temp_inviter = {}
    temp_inviter_id = None
    if inviter is not None:
        temp_inviter = {
            'first_name': inviter.first_name,
            'last_name': inviter.last_name,
            'username': inviter.username,
            'email': inviter.email,
            'phone': inviter.profile.phone if hasattr(inviter, 'profile') else '',
            'id': inviter.id,
        }

    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'has_error': has_error,
                   'error_message': error_message,
                   'inviter': json.dumps(temp_inviter),
                   'agreements': agreements,
                   'inviter_id': inviter_id if inviter_id else temp_inviter_id is not None if temp_inviter_id else None,
                   'registered': registered})


def manage_activate_user(request):

    id = request.GET.get('id')

    user = User.objects.get(id=id)

    user.is_active = True
    user.save()

    return redirect('manage_userprofile_user_list')


@staff_member_required
@login_required
def manage_generate_user(request):

    if request.method == 'POST':

        prefix = request.POST.get('prefix')
        inviter = request.POST.get('inviter')
        total = request.POST.get('total')

        try:
            inviter_obj = User.objects.get(username=inviter)
        except:
            error_message = " Error: Inviter Does not exist"
            messages.add_message(request, messages.ERROR, error_message)
            return redirect('manage_userprofile_user_list')

        for i in range(1, int(total)+1):
            try:

                year = random.randint(1960, 2000)
                month = random.randint(1, 12)
                date = random.randint(1, 28)

                country_id = random.randint(1, 200)

                try:
                    country = Country.objects.filter(id=country_id).first()
                except:
                    country = Country.objects.filter(id=1).first()

                user = User.objects.create_user(
                    username=prefix + str(i),
                    first_name=prefix + str(i),
                    last_name=prefix + str(i),
                    email=prefix + str(i)+'@' + prefix + str(i)+'.com',
                    password=prefix + str(i),
                    is_active=True,
                )

                Profile.objects.create(
                    user=user,
                    country=country,
                    inviter=inviter_obj,
                    gender=random.randint(0, 1),
                    date_of_birth=datetime(year, month, date),
                    address=str(country),
                    phone='0722'+str(random.randint(000000, 999999)),
                    town=str(country),
                    location=str(country)
                ).save()

            except:
                error_message = " Error: While adding " + prefix + str(i)
                messages.add_message(request, messages.ERROR, error_message)

    return redirect('manage_userprofile_user_list')


@staff_member_required
@login_required
def manage_create_user(request):

    if request.method == 'POST':

        user_form = ManageUserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            inviter_id = request.POST.get('inviter')
            country_id = request.POST.get('country')

            user_data = user_form.cleaned_data
            profile_data = profile_form.cleaned_data

            global_preferences = global_preferences_registry.manager()

            user = User.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
                is_active=True,
            )

            inviter = User.objects.get(id=1)

            try:
                inviter = User.objects.get(id=inviter_id)
            except:
                pass

            Profile.objects.create(
                user=user,
                country=Country.objects.filter(id=country_id).first(),
                inviter=inviter,
                gender=int(profile_data['gender']),
                date_of_birth=profile_data['date_of_birth'],
                address=profile_data['address'],
                phone=profile_data['phone'],
                town=profile_data['town'],
                location=profile_data['town']
            ).save()

            group, created = Group.objects.get_or_create(name='Registered')
            if group:
                user.groups.add(group)

            return redirect('manage_userprofile_user_list')
        else:
            error_message = ''
            error_message = error_message + \
                ' '.join([' '.join(x for x in l)
                          for l in list(user_form.errors.values())])
            error_message = error_message + \
                ' '.join([' '.join(x for x in l)
                          for l in list(profile_form.errors.values())])

            messages.add_message(request, messages.ERROR, error_message)

            return redirect('manage_userprofile_user_create')


def emailVerificationView(request):

    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    status = False
    title = message = ''

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        status = True
        title = 'Email Verification Successful'
        message = 'Thank you for your email confirmation. Now you can login your account.'
    else:
        status = False
        title = 'Email Verification Failed'
        message = 'Activation link is invalid!'

    context = {
        'status': status,
        'title': title,
        'message': message,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'email-verification.html', context=context)


def registerThankView(request):

    code = ""
    email = ""
    error = False
    message = "Everything is ok."

    global_preferences = global_preferences_registry.manager()

    verification_by_code = global_preferences['userprofile__verification_by_code']

    if request.method == 'POST':

        posted_code = request.POST.get('code')

        profile = Profile.objects.filter(code=posted_code).first()

        code = profile.code
        email = profile.user.email

        if int(profile.code) == int(posted_code):

            profile.code = None
            profile.save()

            if profile.user:
                profile.user.is_active = True
                profile.user.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Your account is now verified.')

            return redirect('user_dashboard')
        else:
            error = True
            message = "Verification Code provided is incorrect."

    context = {
        'title': "Thank you for Registering",
        'error': error,
        'code': code,
        'message': message,
        'verification_by_code': verification_by_code,
        'registered_email': email
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'register-thank.html', context=context)


@login_required
def manage_change_password(request):
    """View function for homepage of site."""

    if request.POST:
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')

        user = User.objects.get(id=user_id)

        is_valid = True

        if password != password_again:
            messages.add_message(request, messages.ERROR,
                                 'Password Entered Did not match.')
            is_valid = False

        if len(password) < 6:
            messages.add_message(
                request, messages.ERROR, 'Password too short. It should be more than 6 characters')
            is_valid = False

        if is_valid:
            messages.add_message(request, messages.SUCCESS,
                                 'Password Changed Successfully.')
            user.set_password(password)
            user.save()

            return redirect('manage_userprofile_user_update', pk=user_id)
        else:
            return redirect('manage_userprofile_user_update', pk=user_id)
    else:
        return redirect('manage_userprofile_user_list')


@login_required
def manage_change_group_permissions(request):
    """View function for homepage of site."""

    if request.POST:
        group_id = request.POST.get('group_id')
        action = request.POST.get('action')
        permission = request.POST.get('permission')

        permission_arr = permission.split(':')

        group = Group.objects.filter(id=group_id).first()

        content_type = ContentType.objects.get(
            app_label=permission_arr[0], model=permission_arr[1])
        permission = Permission.objects.get(
            codename=permission_arr[2], content_type=content_type)

        if action == 'add':
            group.permissions.add(permission)
        else:
            group.permissions.remove(permission)

    message = {
        'status': 200,
        'message': 'Permission changed Successfully ',
    }

    return JsonResponse(message)


@login_required
def manage_change_user_groups(request):
    """View function for homepage of site."""

    if request.POST:
        user_id = request.POST.get('user_id')
        group_id = request.POST.get('group_id')
        action = request.POST.get('action')

        group = Group.objects.filter(id=group_id).first()
        user = User.objects.get(id=user_id)

        if action == 'add':
            user.groups.add(group)
        else:
            user.groups.remove(group)

    message = {
        'status': 200,
        'message': 'Group changed Successfully ',
    }

    return JsonResponse(message)


def fetchInviterView(request):

    inviter_username = request.GET.get('inviter_username')

    inviter = None

    try:
        inviter = User.objects.get(username=inviter_username)
    except:
        pass

    if inviter:
        temp_inviter = {
            'first_name': inviter.first_name,
            'last_name': inviter.last_name,
            'username': inviter.username,
            'email': re.sub(r'(?<=\w{4})\w(?=\w*@)', 'x', inviter.email) if inviter.email else '' ,
            'phone': re.sub(r'(?<=\d{4})\d(?=\d{3})', 'x', inviter.profile.phone) if hasattr(inviter, 'profile') and inviter.profile.phone else '',
            'id': inviter.id,
        }
    else:
        temp_inviter = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',
            'phone': '',
            'id': 0,
        }

    return JsonResponse(temp_inviter)


def checkUserView(request):

    has_error = False
    error_message = ''

    username = request.GET.get('username')
    email = request.GET.get('email')

    if username:
        existing_username = User.objects.filter(username=username).all()
        if existing_username:
            error_message = error_message + ' Username is Aready Taken.'
            has_error = True

    if email:
        existing_email = User.objects.filter(email=email).all()
        if existing_email:
            error_message = error_message + ' Email is Aready Taken.'
            has_error = True

    temp_data = {
        'error_message': error_message,
        'has_error': has_error,
    }

    return JsonResponse(temp_data)


def locationApi(request):

    country_id = request.GET.get('country_id')
    locations_arr = []

    country = Country.objects.filter(id=country_id).first()
    locations = Location.objects.filter(country_code=country.code).all()

    for location in locations:

        location_obj = {
            'id': location.id,
            'name': location.name,
            'country_code': location.country_code,
            'state_code': location.state_code,
        }

        locations_arr.append(location_obj)

    return JsonResponse(locations_arr, safe=False)


"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""


"""------------------- User ---------------------- """


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileUserView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = User
    table_class = ManageUserprofileUserTable
    template_name = 'manage/userprofile_user_list.html'

    filterset_class = ManageUserprofileUserFilter

    permission_required = 'userprofile.view_user'

    paginate_by = 20

    ordering = ['-id']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['limit'] = int(self.request.GET.get('limit', 20))

        return context

    def get_paginate_by(self, queryset):

        limit = self.request.GET.get('limit')

        self.paginate_by = limit if limit else self.paginate_by

        return self.paginate_by


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileUserCreate(PermissionRequiredMixin, CreateView):
    template_name = 'manage/userprofile_user_form_new.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'is_active']
    permission_required = 'userprofile.add_user'

    def get_context_data(self, **kwargs):

        field_attr = {'class': 'record-picker',
                      'readonly': True, 'addon_after_class': None}

        common = Common()

        context = super().get_context_data(**kwargs)
        user_form = ManageUserForm()
        profile_form = ProfileForm()

        inviter_attr = field_attr.copy()
        inviter_attr['addon_after'] = common.recordPickerButton(
            'inviter', 'manage_userprofile_user_list')

        profile_form.fields['inviter'].widget = forms.TextInput(
            attrs=inviter_attr)

        context['user_form'] = user_form
        context['profile_form'] = profile_form

        return context

    def get_success_url(self):
        return reverse('manage_userprofile_user_update', args=[str(self.id)])


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileUserUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'manage/userprofile_user_form.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'is_active']

    permission_required = 'userprofile.change_user'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['groups'] = Group.objects.filter().all()
        context['user_groups'] = context['object'].groups.all()

        return context

    def get_success_url(self):
        return reverse('manage_userprofile_user_update', args=[str(self.object.id)])


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileProfileUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'manage/userprofile_profile_form.html'
    model = Profile
    fields = ['gender', 'date_of_birth', 'country', 'inviter',
              'address', 'phone', 'town', 'location', 'blocked']

    permission_required = 'userprofile.change_user'

    def get_form(self, form_class=None):

        common = Common()

        field_attr = {'class': 'record-picker',
                      'readonly': True, 'addon_after_class': None}

        inviter_attr = field_attr.copy()
        inviter_attr['addon_after'] = common.recordPickerButton(
            'inviter', 'manage_userprofile_user_list')

        form = super(ManageUserprofileProfileUpdate, self).get_form(form_class)
        form.fields['inviter'].widget = forms.TextInput(attrs=inviter_attr)
        return form

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.profile

    def get_success_url(self):
        return reverse('manage_userprofile_profile_update', args=[str(self.object.user_id)])


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileUserDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'manage/userprofile_user_confirm_delete.html'
    model = User
    success_url = reverse_lazy('manage_userprofile_user_list')
    permission_required = 'userprofile.delete_user'


"""------------------- Group ---------------------- """


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileGroupView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Group
    table_class = ManageUserprofileGroupTable
    template_name = 'manage/userprofile_group_list.html'

    filterset_class = ManageUserprofileGroupFilter

    permission_required = 'userprofile.view_group'

    paginate_by = 20

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['limit'] = int(self.request.GET.get('limit', 20))

        return context

    def get_paginate_by(self, queryset):

        limit = self.request.GET.get('limit')

        self.paginate_by = limit if limit else self.paginate_by

        return self.paginate_by


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileGroupCreate(PermissionRequiredMixin, CreateView):
    template_name = 'manage/userprofile_group_form.html'
    model = Group
    fields = ['name', ]
    permission_required = 'userprofile.add_group'

    def get_success_url(self):
        return reverse('manage_userprofile_group_update', args=[str(self.object.id)])


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileGroupUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'manage/userprofile_group_form.html'
    model = Group
    fields = ['name', ]

    permission_required = 'userprofile.change_group'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        apps = []

        group_permissions = context['object'].permissions.all()
        app_list = ContentType.objects.values('app_label').distinct()

        for app_item in app_list:

            modules = []

            app_name = app_item['app_label']

            module_list = ContentType.objects.filter(
                app_label=app_name).values('model').distinct()

            for module_item in module_list:

                module_name = module_item['model']

                permissions = Permission.objects.filter(
                    content_type__app_label=app_name, content_type__model=module_name).all()

                module_dict = {'name': module_name, 'permissions': permissions}

                if permissions:
                    modules.append(module_dict)

            app_dict = {'name': app_name, 'modules': modules}

            if modules:
                apps.append(app_dict)

        context['apps'] = apps
        context['group_permissions'] = group_permissions

        return context

    def get_success_url(self):
        return reverse('manage_userprofile_group_update', args=[str(self.object.id)])


@method_decorator(login_required(login_url='login'), name="dispatch")
class ManageUserprofileGroupDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'manage/userprofile_group_confirm_delete.html'
    model = Group
    success_url = reverse_lazy('manage_userprofile_group_list')
    permission_required = 'userprofile.delete_group'
