from django.db import models

# Create your models here.


class SystemTrackModel(models.Model):

    is_modified = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, db_index=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, editable=False, related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, editable=False, related_name='%(app_label)s_%(class)s_updated')

    class Meta:
        abstract = True


