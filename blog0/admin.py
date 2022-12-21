from django.contrib import admin
from blog0.models import Photo, Category, Commant

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'price', 'localisation', 'contact', 'date_added', 'active')

admin.site.register(Photo, PhotoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class CommantAdmin(admin.ModelAdmin):
    list_display = ['photo', 'username', 'email','body']

admin.site.register(Commant, CommantAdmin)