from django.conf.global_settings import STATIC_ROOT
from django.conf.urls.static import static
from django.urls import path

from main.settings import *
from quiz_app.views.quiz_views import *

app_name = 'quiz'

urlpatterns = [
    path('', QuizListViews.as_view(), name='main-view'),
    path('<id>/', quiz_views, name='quiz-view'),
    path('<id>/data/', quiz_data_views, name='quiz-data-view'),
    path('<id>/submit/', quiz_submission_view, name='quiz-submission-view'),
]
if DEBUG:
    urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
