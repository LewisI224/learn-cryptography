from turtle import title
from django.shortcuts import render
from .models import LearningModules
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

modules = LearningModules.objects.all()
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

def Module(request):
    module = LearningModules.objects.get(pagePath=reverse(Module))
    pageUrl = module.learningPage
    Profile.objects.filter(pk=request.user.profile.pk).update(currentLevel=module.title)
    return render(request, pageUrl)