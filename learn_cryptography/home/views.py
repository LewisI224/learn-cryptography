from django.shortcuts import render

modules = [
    {
        'title': 'Intro to Cryptography',
        'difficulty': 'Beginner',
        'time': '10',
        'description': 'An introduction to learning using this website and some of the history of cryptography.',
        'image': '/home/intro_to_cryptography.jpg', 
    },
    {
        'title': 'Caesar Cipher',
        'difficulty': 'Intermediate',
        'time': '5',
        'description': 'The Caesar cipher is a simple substitution cipher used by the Roman general Julius Caesar during his campaigns. In this module learn the basics of using the Caesar Cipher and also techniques for forcefully decoding messages encrypted using it.',
        'image': '/home/caesar_cipher.jpg', 
    },
    {
        'title': 'Vigenere Cipher',
        'difficulty': 'Advanced',
        'time': '15',
        'description': 'Building upon the Caesar Cipher is the Vigenère. It uses a series of Caesar ciphers to encrypt a message according to a chosen keyword. This module teaches how to use this cipher and also how to break it ;)',
        'image': '/home/vigenere_cipher.jpg',        
    },
]
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

def learning(request):
    context = {
        'modules' : modules,
        'title' : 'learning'
    }
    return render(request, 'home/learning.html', context)
