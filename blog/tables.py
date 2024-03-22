import django_tables2 as tables

from .models import Blog

from django.utils.safestring import mark_safe

"""xxxxxxxxxxxxxxxxxxxxx Manage Section xxxxxxxxxxxxxxxxxxxx"""

action_links = """   {% if not global_recordpicker %}  


    <div class="dropdown user user-menu">
		<a href="/manage/#" class="btn btn-primary btn-sm waves-effect waves-light dropdown-toggle" data-bs-toggle="dropdown" title="User">
			<i class="fas fa-cog"></i>
		</a>
	    <ul class="dropdown-menu animated flipInX">
			<li class="user-body">
                <a class="dropdown-item p-1" href="{% url "manage_blog_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
                <a class="dropdown-item p-1" href="{% url "manage_blog_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
			</li>
		</ul>
	</div>

{% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.title }} {{ record.business }}" type="button">Select</button>{% endif %}"""

class ManageBlogTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    featured_image = tables.Column()
    title = tables.Column()
    slug = tables.Column()
    category = tables.Column()
    hits = tables.Column()
    published = tables.Column()
    featured = tables.Column()
    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }

    def render_featured_image(self, value, record):

        return mark_safe("<img width='100px' src='/uploads/%s'>" % (record.featured_image)) 
       


action_links = """   {% if not global_recordpicker %}  


    <div class="dropdown user user-menu">
		<a href="/manage/#" class="btn btn-primary btn-sm waves-effect waves-light dropdown-toggle" data-bs-toggle="dropdown" title="User">
			<i class="fas fa-cog"></i>
		</a>
	    <ul class="dropdown-menu animated flipInX">
			<li class="user-body">
                <a class="dropdown-item p-1" href="{% url "manage_blog_category_update" record.pk %}"><i class="fas fa-pencil-alt"></i> Edit</a> 
                <a class="dropdown-item p-1" href="{% url "manage_blog_category_delete" record.pk %}"><i class="fas fa-trash"></i> Delete</a>
			</li>
		</ul>
	</div>


  {% else %} <button class="btn btn-primary btn-sm recordpicker-select" data-record_id="{{ record.pk }}"  data-record_text="{{ record.title }}" type="button">Select</button>{% endif %}"""

class ManageBlogCategoryTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)
    featured_image = tables.Column()
    title = tables.Column()
    slug = tables.Column()
    published = tables.Column()
    featured = tables.Column()   

    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }

    def render_featured_image(self, value, record):

        return mark_safe("<img width='100px' src='/uploads/%s'>" % (record.featured_image))


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
    featured_image = tables.Column()
    title = tables.Column()
    slug = tables.Column()
    published = tables.Column()
    featured = tables.Column()   
    manage = tables.TemplateColumn(action_links,verbose_name=u'',)

    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }

    def render_featured_image(self, value, record):

        return mark_safe("<img width='100px' src='/uploads/%s'>" % (record.featured_image)) 
       


class UserBlogCategoryTable(tables.Table):
    ''' action = tables.CheckBoxColumn(verbose_name="Amend", accessor="pk")'''
    featured_image = tables.Column()
    title = tables.Column()
    slug = tables.Column()
    published = tables.Column()
    featured = tables.Column()   

    class Meta:

        attrs = {
            'class': 'table table-hover table-sm',
            'thead' : {
                'class': 'head-dark'
            }
        }

    def render_featured_image(self, value, record):

        return mark_safe("<img width='100px' src='/uploads/%s'>" % (record.featured_image))




"""xxxxxxxxxxxxxxxxxxxxx User Section xxxxxxxxxxxxxxxxxxxx"""
