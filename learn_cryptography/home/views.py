from django.shortcuts import render

modules = [
    {
        'title': 'Scytale',
        'difficulty': 'Beginner',
        'time': '5',
        'description': 'Scytale - a wooden rod which parchment would be wound around',
    },
    {
        'title': 'Caesar Cipher',
        'difficulty': 'Beginner',
        'time': '10',
        'description': 'A substitution cipher used since ancient times',
    }
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
