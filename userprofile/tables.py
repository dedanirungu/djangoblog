import django_tables2 as tables


"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""

action_links = """  {% if not global_recordpicker %} <div class="dropdown">
    <button class="btn btn-outline-primary btn-sm btn-outline dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <i class="fas fa-cog"></i>
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a class="dropdown-item p-1" href="{% url "manage_userprofile_user_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit User</a> 
        <a class="dropdown-item p-1" href="{% url "manage_userprofile_profile_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit Profile</a> 
        <a class="dropdown-item p-1" href="{% url "manage_userprofile_user_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
    </div>
  </div>{% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.first_name }} {{ record.last_name }}({{ record.username }}){{ record.email }}" type="button">Select</button>{% endif %}"""


action_is_active = """ 
    {% if not record.is_active %}
        <a href="{% url "manage_activate_user" %}?id={{ record.pk }}">Activate</a>
    {% else %}
        TRUE
    {% endif %}
"""

class ManageUserprofileUserTable(tables.Table): 
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    id = tables.Column()
    first_name = tables.Column()
    last_name = tables.Column()
    username = tables.Column()
    email = tables.Column()
    profile__inviter = tables.Column()
    profile__gender = tables.Column()
    profile__phone = tables.Column()
    profile__country = tables.Column()
    profile__date_of_birth = tables.Column()
    date_joined = tables.Column()
    last_login = tables.Column()
    is_staff = tables.Column()
    is_active = tables.TemplateColumn(action_is_active, verbose_name=u'Active',)

    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }



action_links = """   {% if not global_recordpicker %}   <div class="dropdown">
    <button class="btn btn-outline-primary btn-sm btn-outline dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <i class="fas fa-cog"></i>
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a class="dropdown-item p-1" href="{% url "manage_userprofile_group_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
        <a class="dropdown-item p-1" href="{% url "manage_userprofile_group_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
    </div>
  </div>{% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.name }}" type="button">Select</button>{% endif %}"""
class ManageUserprofileGroupTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    id = tables.Column()
    name = tables.Column()
    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }





"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""
