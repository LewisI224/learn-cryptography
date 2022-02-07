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
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    required_score_to_pass = models.IntegerField()

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

