from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    edit_photo = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Photo
        fields = ['image', 'caption','price','localisation', 'contact', 'categories', 'description', 'active']


class CommantForm(forms.ModelForm):
    class Meta:
        model = models.Commant
        fields = ['username', 'email','body']
