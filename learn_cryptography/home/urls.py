from django.urls import path
from . import views


urlpatterns = [
    path('learning/', views.learning, name='learning'),
    path('about/', views.about, name='public-about'),
    path('', views.home, name='public-home'),
    
]