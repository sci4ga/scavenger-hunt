from django.conf import settings
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

# Create your models here.

'''
TODO for code friendly DB model

Tables:
    Quiz
        Title
        Location
    Questions
        quiz ID
        question number
        question text
        correct answer
        choices (array)
    Responses
        user ID
        question ID
        response
'''
def answer_field():
    return models.CharField(max_length=500, db_index=True)

class Quiz(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    location = models.CharField(max_length=100, db_index=True)

class Question(models.Model):
    quiz = models.ForeignKey(
        to='Quiz', 
        on_delete=models.CASCADE
    )
    question_number = models.PositiveSmallIntegerField(db_index=True)
    question_text = models.TextField(db_index=True)
    correct_answer = answer_field()
    choices = ArrayField(
        base_field=answer_field(), 
        null=True,
        blank=True
    )

class Response(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        to='Question',
        on_delete=models.CASCADE
    )
    response = answer_field()