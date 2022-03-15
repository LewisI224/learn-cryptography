from django.urls import path
from . import views

urlpatterns = [
    
    path('introtocrypto/', views.Module , name='crypto-module'),
    path('introtocrypto/quiz/', views.quiz , name='crypto-quiz'),
    path('caesar/', views.Module , name='caesar-module'),
    path('caesar/quiz/', views.quiz , name='caesar-quiz'),
    path('vigenere/', views.Module , name='vigenere-module'),
    path('vigenere/quiz/', views.quiz , name='vigenere-quiz'),
    path('fun-ciphers/', views.Module , name='fun-ciphers-module'),
    path('fun-ciphers/quiz/', views.quiz , name='fun-ciphers-quiz'),
    path('encryption-vs-encoding/', views.Module , name='encryption-vs-encoding-module'),
    path('encryption-vs-encoding/quiz/', views.quiz , name='encryption-vs-encoding-quiz'),
    path('asymmetric-cryptography/', views.Module , name='asymmetric-module'),
    path('asymmetric-cryptography/quiz/', views.quiz , name='asymmetric-quiz'),
    
    path('completed', views.complete , name='completed-learning'),
    
    path('', views.learning , name='learning'),
    
]