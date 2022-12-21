from django.shortcuts import render, get_object_or_404
from blog0.models import Photo, Commant
from django.shortcuts import redirect, render
from . import forms, models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def home(request):
    photos = models.Photo.objects.all()
    paginator = Paginator(photos, 6)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request, 'blog0/home.html', context={'photos': photos})

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('index')
    return render(request, 'blog0/photo_upload.html', context={'form': form})

@login_required
def index(request):
    photos = Photo.objects.all()
    return render(request, "app/index.html", context ={'photos': photos})
       
def search(request):
    query = request.GET["photo"]
    liste_photo = Photo.objects.filter(caption__contains=query)
    return render(request, "blog0/search.html", {"liste_photo": liste_photo})
        
def detail(request,id_photo):
    photo = Photo.objects.get(id=id_photo)
    commants = Commant.objects.filter(photo=id_photo)
    new_commant = None
    if request.method == 'POST':
        commant_form = forms.CommantForm(data=request.POST)
        if commant_form.is_valid():
            new_commant = commant_form.save(commit=False)
            new_commant.photo =  photo
            new_commant.save()
    else:
        commant_form = forms.CommantForm()
    return render(request, 'blog0/detail.html', {"photo": photo, "commants":commants, "new_commant":new_commant, "commant_form":commant_form})


def edit_photo(request, id_photo):
    photo = get_object_or_404(models.Photo, id=id_photo)
    edit_form = forms.PhotoForm(instance=photo)
    if request.method == 'POST':
        if 'edit_photo' in request.POST:
            edit_form = forms.PhotoForm(request.POST, instance=photo)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('index')
                
    context = {'edit_form': edit_form}
    return render(request, 'blog0/edit_photo.html', context=context)

@login_required
def delete_photo(request, id_photo):
    photo = get_object_or_404(models.Photo, id=id_photo)
    name = Photo.caption
    if request.method == 'POST':
        photo.delete()
        return redirect('index')

    return render(request, 'blog0/delete.html', {"name":name})