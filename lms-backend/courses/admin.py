from django.contrib import admin
from .models import Course, Module, ContentItem, QuizQuestion

# Register your models here.

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(ContentItem)
admin.site.register(QuizQuestion)
