from django.conf import settings
from django.db import models

# Create your models here.
'''
timeline, a list of quizzes, with progress through the quiz
each quiz has a list of questions that need to be answered

'''

class Quiz(models.Model):
    quiz_number = models.PositiveSmallIntegerField(primary_key = True)
    title = models.CharField(max_length = 50, db_index = True)

class Question(models.Model):
    quiz = models.ForeignKey(
        to = 'Quiz',
        on_delete = models.CASCADE
    )
    question_number = models.PositiveSmallIntegerField(db_index = True)
    question = models.TextField(db_index = True)
    

class QuestionOption(models.Model):
    question = models.ForeignKey(
        to = 'Question',
        on_delete = models.CASCADE
    )
    text_option = models.CharField(max_length = 100, db_index = True, null = True, blank = True)
    number_option = models.DecimalField(
        max_digits = 50,
        decimal_places = 25,
        db_index = True, 
        null = True, 
        blank = True
    )
    integer_option = models.IntegerField(db_index = True, null = True, blank = True)
    option_display = models.TextField(null = True, blank = True)

class Answer(models.Model):
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    question = models.ForeignKey(
        to = 'Question',
        on_delete = models.CASCADE
    )
    option_answer = models.ForeignKey(
        to = 'QuestionOption',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    text_answer = models.TextField(null = True, blank = True)
    number_answer = models.DecimalField(
        max_digits = 50,
        decimal_places = 25,
        null = True, 
        blank = True
    )
    integer_answer = models.IntegerField(null = True, blank = True)
