from __future__ import unicode_literals
# import re
from django.db import models
from datetime import datetime, date

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if(len(postData['title'])) < 2:
            errors['title'] = "El titulo debe tener a los menos 2 caractéres"
        
        if(len(postData['network'])) < 3:
            errors['network'] = "El network debe tener a los menos 3 caractéres"
        
        if len(postData['release_date']) < 8:
            errors['release_date'] = "Fecha lanzamiento no tiene largo correcto"
        
        if len(postData['description']) < 10:
            errors['description'] = "La descripción debe tener a los menos 3 caractéres"
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length=250)
    network = models.CharField(max_length=250)
    release_date = models.DateField(auto_now_add = False, auto_now= False, blank= True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()