from email.mime import image
from django.db import models

class LearningModules(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="/home/intro_to_cryptography.jpg")
    description = models.TextField()
    difficulty = models.CharField(max_length=15)
    time = models.IntegerField()
    learningPage = models.CharField(max_length=100, default="default")

    def __str__(self):
        return self.title