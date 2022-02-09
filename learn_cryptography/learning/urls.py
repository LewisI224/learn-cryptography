from django.urls import path
from . import views

urlpatterns = [
    
    path('introtocrypto/', views.Module , name='crypto-module'),
    path('introtocrypto/quiz', views.quiz , name='crypto-quiz'),
    path('completed', views.complete , name='completed-learning'),
    path('', views.learning , name='learning'),
    
]