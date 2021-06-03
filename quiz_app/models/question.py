from django.db import models

from base.models import BaseModel
from quiz_app.models.quiz import Quiz


class Question(BaseModel):
    question_text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        app_label = 'quiz_app'
