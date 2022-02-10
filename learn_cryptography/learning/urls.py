from django.urls import path
from . import views

urlpatterns = [
    
    path('introtocrypto/', views.Module , name='crypto-module'),
    path('caesar/', views.Module , name='caesar-module'),
    path('caesar/quiz', views.quiz , name='caesar-quiz'),
    path('introtocrypto/quiz', views.quiz , name='crypto-quiz'),
    path('completed', views.complete , name='completed-learning'),
    
    path('', views.learning , name='learning'),
    
]