from django.shortcuts import render
from .models import LearningModules, Quiz, Question, Answer
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

modules = LearningModules.objects.all()
@login_required
def learning(request, tag=None, sort=None):
    titles = []
    cmpld = []
    modules = (list(request.user.profile.completedModules.values('title')))
    for title in modules:
            titles.append(list(title.values()))
    characters = "[]'"
    for l in titles:
        cmpld.append(str(l).strip(characters))
    titles = ','.join(cmpld)

    if tag:
        modules = LearningModules.objects.filter(tags__name__in=[tag])
    else:
        modules = LearningModules.objects.all()
    if sort:
        if (sort=="time"):
            modules=LearningModules.objects.all().order_by("time")
        elif(sort=="difficulty"):
            modules=LearningModules.objects.all().order_by("difficultyNumber")
        elif(sort=="suggested"):
            modules=LearningModules.objects.all().order_by("suggestedOrder")

    tags = LearningModules.tags.all()
    context = {
        'modules' : modules,
        'completed': titles,
        'title' : 'learning',
        'tags':tags,
        'tag': tag,
        'sort':sort,
    } 

    return render(request, 'learning/learning.html', context)

def Module(request):
    module = LearningModules.objects.get(pagePath=request.get_full_path())
    pageUrl = module.learningPage
    Profile.objects.filter(pk=request.user.profile.pk).update(currentLevel=module.title)
    text_string = module.text
    context = {
        'title':module.title,
        'text':text_string,
        'glossary':module.glossary,
        'image':module.image,
        'quizPath':module.quizPath,
        'numberDocuments':module.numberDocuments,
        
    }
    return render(request, pageUrl, context)

def quiz(request):
    Aquiz = Quiz.objects.get(assosPage=request.get_full_path())
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
    completedModule = LearningModules.objects.get(title=request.user.profile.currentLevel)
    updScore = currScore + 100
    profile = Profile.objects.get(pk=request.user.profile.pk)
    profile.completedModules.add(completedModule)
    Profile.objects.filter(pk=request.user.profile.pk).update(score=updScore)
    Profile.objects.filter(pk=request.user.profile.pk).update(currentLevel="Nothing")
    return redirect('learning')

def tags(request):
    tag = request.get_full_path()
    tag = tag.strip("/")
    return learning(request, tag=tag, sort=None)

def sort(request):
    sort = request.get_full_path()
    sort = sort.strip("/")
    return learning(request, tag=None, sort=sort)

