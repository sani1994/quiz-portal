from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from quiz_app.models.question import Question
from quiz_app.models.quiz import Quiz

ANSWER_WEIGHT = 1


class QuizListViews(ListView):
    model = Quiz
    template_name = 'quiz_list_view.html'


def quiz_views(request, id):
    quiz = Quiz.objects.filter(id=id).last()
    return render(request, 'quiz.html', {'obj': quiz})


def quiz_data_views(request, id):
    quiz = Quiz.objects.filter(id=id).last()
    questions = []
    for q in quiz.get_questions():
        answer = list(q.answer_set.all().values_list('answer_text', flat=True))
        questions.append({q.question_text: answer})
    return JsonResponse({
        'data': questions,
        'time': quiz.time_duration
    })


def quiz_submission_view(request, id):
    quiz = Quiz.objects.filter(id=id).last()
    multiplexer = 100 / quiz.score_to_pass
    pass_score = (quiz.no_of_questions * ANSWER_WEIGHT) * multiplexer
    datas = request.POST
    datas = dict(datas.lists())  # convert querydict to normal dict
    datas.pop('csrfmiddlewaretoken')
    correct_ans = 0
    wrong_ans = 0
    earned_score = 0
    is_pass = False

    for k, v in datas.items():
        question = Question.objects.filter(question_text=k).last()
        if question:
            correct_answers = question.answer_set.filter(is_correct=True).values_list('answer_text', flat=True)
            if v[0] in correct_answers:
                correct_ans += 1
            else:
                wrong_ans += 1
    if correct_ans > 0:
        earned_score = correct_ans * ANSWER_WEIGHT
        if earned_score >= pass_score:
            is_pass = True

    return JsonResponse({
        'quiz_name': quiz.name,
        'correct_ans': correct_ans,
        'wrong_ans': wrong_ans,
        'earned_score': earned_score,
        'pass': is_pass
    })
