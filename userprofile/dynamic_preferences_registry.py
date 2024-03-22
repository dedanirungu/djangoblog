
from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry

# we create some section objects to link related preferences together

userprofile = Section('userprofile')
 
# We start with a global preference
@global_preferences_registry.register
class EmailVerification(BooleanPreference):
    section = userprofile
    name = 'email_verification'
    default = False
    required = False

    # We start with a global preference
@global_preferences_registry.register
class VerificationByCode(BooleanPreference):
    section = userprofile
    name = 'verification_by_code'
    default = False
    required = False 
       
