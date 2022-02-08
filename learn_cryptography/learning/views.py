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
    Aquiz = Quiz.objects.get(assosPage=reverse(quiz))
    questions_list = list(Question.objects.filter(quiz=Aquiz))
    answers_dict = {}
    for i in range(len(questions_list)):
        answers = Answer.objects.filter(question=(questions_list[i]))
        answers_dict[i] = ((list(answers)))
   
    context = {
        'quiz': Aquiz,
        'questions': questions_list,
        'answers': answers_dict,
        'title': 'quiz',
    }
    return render(request, 'learning/introtocrypto_quiz.html', context)