from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
