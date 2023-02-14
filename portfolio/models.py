from django.db import models
from django.db.models.fields import CharField
from django.forms import ImageField, URLField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)