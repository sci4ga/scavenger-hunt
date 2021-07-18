from django.shortcuts import render
from django.views.generic.base import TemplateView 

# Create your views here.
def home(request):
    return render(request = request,
                  template_name='main/home.html')
