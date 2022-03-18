import random

from django.db import models
from taggit.managers import TaggableManager

difficulties = [('Beginner','BEGINNER'), ('Intermediate','INTERMEDIATE'), ('Advanced','ADVANCED ')]

class LearningModules(models.Model):
    title = models.CharField(max_length=100, default="Module Title")
    image = models.CharField(max_length=100, default="/learning/default.jpg")
    description = models.TextField(default="A short description of the module content")
    difficulty = models.CharField(choices=difficulties, max_length=15, default='BEGINNER')
    time = models.IntegerField(default=0)
    difficultyNumber = models.IntegerField(default=0)
    suggestedOrder = models.IntegerField(default=0)
    learningPage = models.CharField(max_length=100, default="default")
    pagePath = models.CharField(max_length=100, default="error404")
    quizPath = models.CharField(max_length=100, default="quiz")
    tags = TaggableManager()
    text = models.TextField(default="The learning content for the module with each page seperated witha colon;")
    glossary = models.TextField(default="A list of technical words and their definitions")

    def __str__(self):
        return self.title



class Quiz(models.Model):
    title = models.CharField(max_length=120, default='title')
    assosPage = models.CharField(max_length=120, default='Page Path')
    htmlPage = models.CharField(max_length=120, default='HTML Path')
    number_of_questions = models.IntegerField()
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    module = models.OneToOneField(LearningModules, on_delete=models.CASCADE, default="")
    assosModule = models.CharField(max_length=100, default="error404")
    def __str__(self):
        return self.title
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

class Question(models.Model):
    title = models.TextField(max_length=100, default='title')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + self.quiz.__str__()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
