from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='public-about'),
    path('', views.home, name='public-home'),
    
]