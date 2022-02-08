from django.db import models
import random
difficulties = [('Beginner','BEGINNER'), ('Intermediate','INTERMEDIATE'), ('Advanced','ADVANCED ')]

class Tag(models.Model):
    tag = models.CharField(max_length=35)

    def __str__(self):
        return self.tag

class LearningModules(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="/home/default.jpg")
    description = models.TextField()
    difficulty = models.CharField(choices=difficulties, max_length=15, default='BEGINNER')
    time = models.IntegerField()
    learningPage = models.CharField(max_length=100, default="default")
    pagePath = models.CharField(max_length=100, default="error404")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=120, default='title')
    assosPage = models.CharField(max_length=120, default='Page Path')
    number_of_questions = models.IntegerField()
    required_score_to_pass = models.IntegerField(help_text="required score in %")

    def __str__(self):
        return self.title
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

class Question(models.Model):
    title = models.CharField(max_length=100, default='title')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
