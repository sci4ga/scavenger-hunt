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
