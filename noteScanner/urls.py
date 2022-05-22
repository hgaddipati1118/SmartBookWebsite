from django.urls import path
from noteScanner import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', views.noteScanner, name='hello_world'),      
      path('processImage', processImage, name = 'processImage'),
    path('success', success, name = 'success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)