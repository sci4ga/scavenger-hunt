from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Quiz, Question, QuestionOption
from django.conf import settings

# Create your views here.
def home(request):
    current_quiz = ''
    # get the current quiz the user is on
    return render(
        request = request,
        template_name='main/home.html',
        context = {
            'user': request.user,
            'quizzes': Quiz.objects.all
            # get all questions for current quiz
            # get all question options for each question that has options
        }
    )
