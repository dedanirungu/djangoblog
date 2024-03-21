from django.db import models
from common.models import SystemTrackModel

# Model for storing category of blog
class Category(SystemTrackModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published = models.BooleanField(blank=True, null=True, default=0)

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
    description = models.TextField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(blank=True, null=True, default=0)   
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '%s -- %s' % (self.title, self.category.title)
