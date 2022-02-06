from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('learning/', views.learning , name='learning'),
    path('learning/introtocrypto/', views.Module , name='module'),
    path('about/', views.about, name='public-about'),
    path('register/', user_views.register, name='register'),
    path('', views.home, name='public-home'),
    
]