from django.db import models
from common.models import SystemTrackModel

# Model for storing category of blog
class Category(SystemTrackModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=191, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    published = models.BooleanField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['-id']
        app_label = 'blog'

    def save(self, *args, **kwargs):
        db_manager = DBManager()
        db_manager.save(self)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.SUCCESS, 'Record Created Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_update', args=[str(self.id)])


    def get_delete_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.ERROR, 'Record Deleted Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_delete', args=[str(self.id)])


    def get_update_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.SUCCESS, 'Record Updated Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_update', args=[str(self.id)])       

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title   
    
# Model for storing blos
class Blog(SystemTrackModel):   
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey('Category',  on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name='%(app_label)s_%(class)s_category')
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=191, blank=True, null=True)
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(blank=True, null=True, default=0)   

    class Meta:
        ordering = ['-id']
        app_label = 'blog'

    def save(self, *args, **kwargs):
        db_manager = DBManager()
        db_manager.save(self)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.SUCCESS, 'Record Created Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_update', args=[str(self.id)])


    def get_delete_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.ERROR, 'Record Deleted Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_delete', args=[str(self.id)])


    def get_update_url(self):
        request_middleware = RequestMiddleware(get_response=None)
        request = request_middleware.get_request()

        messages.add_message(request, messages.SUCCESS, 'Record Updated Successfully')
        """Returns the url to access a particular author instance."""
        return reverse('manage_blog_update', args=[str(self.id)])   
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '%s -- %s' % (self.title, self.category.title)
