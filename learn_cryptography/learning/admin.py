from django.contrib import admin
from .models import LearningModules, Tag

admin.site.register(LearningModules)
admin.site.register(Tag)

from .models import Question, Answer, Quiz

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)