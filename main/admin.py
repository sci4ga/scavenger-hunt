from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, QuestionOption, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question_number',
        'question'
    ]


@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'question', 
                'option_display'
            ]
        }),
        ('Value (choose one)', {
            'fields': [
                'text_option',
                'number_option',
                'integer_option'
            ]
        })
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'user', 
                'question'
            ]
        }),
        ('Answer (choose one)', {
            'fields': [
                'option_answer',
                'text_answer',
                'number_answer',
                'integer_answer'
            ]
        })
    ]

admin.site.register([
    Quiz
])