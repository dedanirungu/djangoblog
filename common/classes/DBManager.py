
from django.db import models
from django.contrib import messages
from common.middleware import RequestMiddleware

from django.forms.models import model_to_dict

class DBManager:

    def save(self,record):

        request_middleware = RequestMiddleware(get_response=None)

        try:
            request = request_middleware.get_request()

            user = request_middleware.current_user()

            if(request.POST.get('save_method') and request.POST.get('save_method')=='copy'):
                record.pk = None

            if not hasattr(record, 'is_dataMigration'): 
                record.is_modified = True
        
            if hasattr(user, 'id') and user.id:
                record.updated_by = user
                if not record.id:
                    record.created_by = user
    
        except:
            pass
        
        return record
    
    def serial_model(self, modelobj):

        modeldict = model_to_dict(modelobj)

        if 'groups' in modeldict:
            del modeldict['groups']

        if 'user_permissions' in modeldict:
            del modeldict['user_permissions']

        if 'password' in modeldict:
            del modeldict['password']

        if hasattr(modelobj, '_meta'):  

            opts = modelobj._meta.fields
            
            for m in opts:
                
                if 'upload_to' in m.__dict__:
                    try:
                        modeldict[m.name] = str(getattr(modelobj, m.name))
                    except:
                        modeldict[m.name] = ''

                if m.is_relation:
                    foreignkey = getattr(modelobj, m.name)
                    if foreignkey:
                        try:
                            modeldict[m.name] = self.serial_model(foreignkey)
                        except:
                            pass

        return modeldict