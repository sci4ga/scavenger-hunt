from django.http.response import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Quiz, Question, Response

# Create your views here.
def home(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {
                      'quizzes': Quiz.objects.all
                  })

def quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404(f'Quiz with ID {quiz_id} does not exist')
    
    questions = quiz.question_set.all
    return render(request = request,
                  template_name='main/quiz.html',
                  context = {
                      'quizzes': Quiz.objects.all,
                      'current_quiz': quiz,
                      'questions': questions
                  })
