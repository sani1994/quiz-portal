from django.contrib import admin
from quiz_app.models.answer import Answer
from quiz_app.models.question import Question
from quiz_app.models.quiz import Quiz
from quiz_app.models.result import Result


class QuizAdmin(admin.ModelAdmin):
    exclude = ['type']


admin.site.register(Quiz, QuizAdmin)


class ResultAdmin(admin.ModelAdmin):
    exclude = ['type']


admin.site.register(Result, ResultAdmin)


class AnswerInLine(admin.TabularInline):
    model = Answer
    exclude = ['type']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    exclude = ['type']


admin.site.register(Question, QuestionAdmin)
