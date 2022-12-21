from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField() 
    caption = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name="photos",default=True )
    date_added = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=True)
    description = models.TextField(default=True, null=False)
    localisation = models.CharField(max_length=255, null=True)
    contact = models.IntegerField(null=True)
    active = models.BooleanField()

    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.caption

class Commant(models.Model):
    photo = models.ForeignKey(Photo, on_delete = models.CASCADE, related_name='commants')
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo.caption
