from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('home-page/', views.home_page, name='home'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)