from django.db import models
from datetime import datetime, date

class Show(models.Model):
    title = models.CharField(max_length=250)
    network = models.CharField(max_length=250)
    release_date = models.DateField(auto_now_add = False, auto_now= False, blank= True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)