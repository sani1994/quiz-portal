from django.db import models

from base.models import BaseModel
from quiz_app.models.question import Question


class Answer(BaseModel):
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.question_text}, answer: {self.answer_text}, is_correct: {self.is_correct}"

    class Meta:
        app_label = 'quiz_app'
