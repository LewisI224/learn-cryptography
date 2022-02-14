from turtle import title
from django.shortcuts import render
from learning.models import LearningModules


def home(request):
    if request.user.is_authenticated:
        try:
            currentModule = LearningModules.objects.get(title=request.user.profile.currentLevel)
        except LearningModules.DoesNotExist:
            currentModule = LearningModules.objects.last()
    else:
        currentModule = None
    
    context = {
        'currentModule': currentModule,
        'modules' : LearningModules.objects.all(),
    }
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

