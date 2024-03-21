from django.db import models

# Create your models here.

Class Blog(models.Model):   # Class is a keyword in Python, so it is capitalized
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return "%"%self.title
