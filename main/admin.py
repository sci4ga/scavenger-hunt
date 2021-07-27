from django.contrib import admin
from .models import Quiz, Question, Response
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register([
    Quiz,
    Response
])
