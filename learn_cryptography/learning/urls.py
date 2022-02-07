from django.urls import path
from . import views

urlpatterns = [
    
    path('introtocrypto/', views.Module , name='module'),
    path('introtocrypto/quiz', views.quiz , name='quiz'),
    path('', views.learning , name='learning'),
    
]