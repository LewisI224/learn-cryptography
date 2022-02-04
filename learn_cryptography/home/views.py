from django.shortcuts import render
from .models import LearningModules
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

@login_required
def learning(request):
    context = {
        'modules' : LearningModules.objects.all(),
        'title' : 'learning'
    }
    return render(request, 'home/learning.html', context)
