import django_tables2 as tables

from .models import Blog

"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""

action_links = """   {% if not global_recordpicker %}   <div class="dropdown">
    <button class="btn btn-outline-primary btn-sm btn-outline dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <i class="fas fa-cog"></i>
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a class="dropdown-item p-1" href="{% url "manage_blog_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
        <a class="dropdown-item p-1" href="{% url "manage_blog_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
    </div>
  </div>{% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.title }} {{ record.business }}" type="button">Select</button>{% endif %}"""

class ManageBlogTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    id = tables.Column()
    business = tables.Column()
    title = tables.Column()
    price = tables.Column()
    featured_image = tables.Column()
    location = tables.Column()
    published = tables.Column()
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
        <a class="dropdown-item p-1" href="{% url "manage_blog_category_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
        <a class="dropdown-item p-1" href="{% url "manage_blog_category_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
    </div>
  </div>{% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.title }}" type="button">Select</button>{% endif %}"""

class ManageBlogCategoryTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    id = tables.Column()
    title = tables.Column()
    published = tables.Column()
    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }



"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""



action_links = """  
        <div style="width:90px;">
        <a class="btn btn-outline-success p-1" href="{% url "user_blog_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
        &nbsp;
        <a class="btn btn-outline-success p-1" href="{% url "user_blog_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
        </div>
    """

class UserBlogTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    business = tables.Column()
    title = tables.Column()
    price = tables.Column()
    featured_image = tables.Column()
    location = tables.Column()
    published = tables.Column()
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }


class UserBlogCategoryTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    title = tables.Column()
    published = tables.Column()
    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }




"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""
