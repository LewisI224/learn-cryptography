from email.mime import image
from django.db import models

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

