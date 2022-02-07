from django.shortcuts import render
from .models import LearningModules, Quiz, Question, Answer
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

modules = LearningModules.objects.all()
@login_required
def learning(request):
    context = {
        'modules' : LearningModules.objects.all(),
        'title' : 'learning'
    } 

    return render(request, 'learning/learning.html', context)

def Module(request):
    module = LearningModules.objects.get(pagePath=reverse(Module))
    pageUrl = module.learningPage
    Profile.objects.filter(pk=request.user.profile.pk).update(currentLevel=module.title)

    context = {
        'title':module.title,
        
    }
    return render(request, pageUrl, context)

def quiz(request):
    Aquiz = Quiz.objects.get(topic=reverse(quiz))
    Aquestion = Question.objects.get(quiz=Aquiz)
    context = {
        'quiz': Aquiz,
        'question': Aquestion,
        'answers': Answer.objects.filter(question=Aquestion),
        'title': 'quiz',
    }
    return render(request, 'learning/introtocrypto_quiz.html', context)