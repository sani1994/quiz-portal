from django.db import models

from base.models import BaseModel


class SurveyQuizAttendee(BaseModel):
    name = models.CharField(max_length=255, help_text='Enter your name', default='')
    email = models.EmailField(help_text='Enter email', default='')
    phone_number = models.CharField(max_length=30, default='')
    survey_count = models.IntegerField(default=0)

    class Meta:
        app_label = 'quiz_app'

    def __str__(self):
        return self.name

    def get_survey_quiz_list(self):
        return self.quiz_set.all()


