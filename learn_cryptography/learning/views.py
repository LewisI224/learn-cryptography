from django.shortcuts import render
from .models import LearningModules, Quiz, Question, Answer
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

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
    page = Aquiz.htmlPage
    questions_list = Question.objects.filter(quiz=Aquiz)
    question_title = []
    answerList = []
    correctAnswers = []

    for i in range(len(questions_list)):
        question_title.append(questions_list[i].title)
        Qanswers = Answer.objects.filter(question=(questions_list[i]))
        answerList.append(list(Qanswers))
        for answer in Qanswers:
            if (answer.correct):
                correctAnswers.append(answer.text)
    correctAnswers = ','.join(correctAnswers)
    question_title = ','.join(question_title)
    context = {
        'quiz': Aquiz,
        'questions': questions_list,
        'Qtitle': question_title,
        'answers_list': answerList,
        'correctAnswers': correctAnswers,
        'title': 'quiz',
    }
    return render(request, page, context)

def complete(request):
    currScore = request.user.profile.score
    updScore = currScore + 100
    Profile.objects.filter(pk=request.user.profile.pk).update(score=updScore)
    return redirect('learning')