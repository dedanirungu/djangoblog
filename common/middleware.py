import threading
import requests

from django.urls import resolve
from django.contrib.auth.models import User
from dynamic_preferences.registries import global_preferences_registry

class RequestMiddleware:

  def __init__(self, get_response, thread_local=threading.local()):
    self.get_response = get_response
    self.thread_local = thread_local
    # One-time configuration and initialization.

  def __call__(self, request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.
    self.thread_local.current_request = request

    response = self.get_response(request)

    query_data = {}
    limit = request.GET.get('limit', None)

    if limit:
      current_url = resolve(request.path_info).url_name
      seach_query = request.GET.items()

      if  request.session.has_key('query_data'):
        query_data = request.session['query_data'] 

      if seach_query:
        new_data = {}

        for key, value in seach_query:
          new_data[key] = request.GET.get(key)
          
        query_data[current_url] = new_data   

      request.session['query_data'] = query_data

    if 'guest_country_code' not in request.session or request.session['guest_country_code'] == None:


      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
      remote_ip = request.META.get('REMOTE_ADDR')

      global_preferences = global_preferences_registry.manager()
      geoip_key = global_preferences['common__geoip_key']
      guest_ip = remote_ip if not x_forwarded_for else x_forwarded_for.split(
                ',')[-1].strip()

      geodata = {'country_code':'KE'}

      if(guest_ip != '127.0.0.1'):
        #result = requests.get('http://api.ipstack.com/' + guest_ip + '?access_key=' + geoip_key)
        #geodata = result.json()
        pass


      request.session['guest_country_code'] = geodata['country_code'] if 'country_code' in geodata else 'US'
      request.session['guest_country'] = geodata

    # Code to be executed for each request/response after
    # the view is called.

    return response

  def return_str(self,):

    request = self.thread_local.current_request

    prefix = 'manage_'

    if not request.POST.get('view') is None:
      prefix = request.POST.get('view') + '_'
    
    return prefix

  def get_request(self,):

    request = self.thread_local.current_request
    
    return request

  def get_session(self,):

    request = self.thread_local.current_request
    
    return request.session

  def current_user(self,):

    request = self.thread_local.current_request

    if(request.user.id):
      return User.objects.get(pk=request.user.pk)
      
    return request.user
        
