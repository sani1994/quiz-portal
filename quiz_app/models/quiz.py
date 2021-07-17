import random

from django.db import models

from base.models import BaseModel
from quiz_app.enums.difficulty_level_enum import DIFFICULTY_CHOICES
from quiz_app.models.survey_user import SurveyQuizAttendee


class Quiz(BaseModel):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    no_of_questions = models.IntegerField(default=0)
    time_duration = models.IntegerField(default=0, help_text="Input time duration of the whole quiz in minutes")
    score_to_pass = models.FloatField(help_text="Input pass mark in %")
    difficulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES)
    attendee = models.ForeignKey(SurveyQuizAttendee, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.no_of_questions]

    class Meta:
        app_label = 'quiz_app'
