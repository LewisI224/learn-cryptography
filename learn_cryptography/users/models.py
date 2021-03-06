from turtle import width
from django.db import models
from django.contrib.auth.models import User
from learning.models import LearningModules
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-pics/default.jpg', upload_to="profile-pics")
    currentLevel = models.CharField(max_length=100, default='Nothing')
    score = models.IntegerField( default=0)
    completedModules = models.ManyToManyField(LearningModules)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)