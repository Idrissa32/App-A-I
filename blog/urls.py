"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog0 import views
from django.conf import settings
from django.conf.urls.static import static
from django.core.files import File
import blog0.views
from django.contrib.auth.views import ( PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('gallery/', views.index, name="index"),
    path("", views.home, name="home"),
    path('change-password/', PasswordChangeView.as_view(
        template_name='app/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='app/password_change_done.html'),
         name='password_change_done'
         ),
    path('detail/<int:id_photo>', views.detail, name="detail"),
    path('recherche/', views.search, name="search"),
    path('upload/', views.photo_upload, name='photo_upload'),
    path('edit/<int:id_photo>', views.edit_photo, name='edit_photo'),
    path('delete/<int:id_photo>', views.delete_photo, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
