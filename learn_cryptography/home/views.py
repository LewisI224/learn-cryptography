from turtle import title
from django.shortcuts import render
from learning.models import LearningModules
from users.models import Profile


def home(request):
    if request.user.is_authenticated:
        try:
            currentModule = LearningModules.objects.get(title=request.user.profile.currentLevel)
        except LearningModules.DoesNotExist:
            currentModule = LearningModules.objects.first()
    else:
        currentModule = None
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    context = {
        'currentModule': currentModule,
        'modules' : LearningModules.objects.all()[:3],
        'profile': profile
    }
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

def leaderboard(request):
    context = {
        'profiles' : Profile.objects.all().order_by("-score")
    }
    
    return render(request, 'home/leaderboard.html', context)

