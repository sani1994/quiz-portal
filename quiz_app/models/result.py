from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel


class Result(BaseModel):
    quiz = models.ForeignKey('quiz_app.Quiz', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=255, default='')
    user_no = models.CharField(max_length=25, default='')
    result = models.FloatField(default=0)

    def __str__(self):
        return self.pk

    class Meta:
        app_label = 'quiz_app'
