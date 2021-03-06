from django.contrib import admin
from .models import LearningModules

admin.site.register(LearningModules)

from .models import Question, Answer, Quiz

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)