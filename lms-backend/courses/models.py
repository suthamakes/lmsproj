from django.db import models
from users.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # only teacher can create
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    module_created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # only teacher can create
    order_number = models.IntegerField()


class ContentItem(models.Model):

    LEARNING_STYLE_TYPES = [
        ('active', 'Active'),
        ('reflective', 'Reflective'),
        ('sensing', 'Sensing'),
        ('intuitive', 'Intuitive'),
        ('visual', 'Visual'),
        ('verbal', 'Verbal'),
        ('sequential', 'Sequential'),
        ('global', 'Global'),
    ]

    CONTENT_TYPES = (
        ("video", "Video"),
        ("pdf", "PDF Document"),
        ("article", "Article / Text Content"),
        ("audio", "Audio"),
        ("image", "Image"),
        ("presentation", "PowerPoint / Slides"),
        ("link", "External Link"),
        ("file", "Other File"),
        ("quiz", "Quiz")
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    content_created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # only teacher can create
    data = models.TextField(null=True, blank=True)
    file_url = models.URLField(max_length=255, blank=True, null=True)
    learning_style_type = models.CharField(max_length=50, choices=LEARNING_STYLE_TYPES)
    difficulty_level = models.IntegerField()
    created_at = models.DateTimeField()


class QuizQuestion(models.Model):

    OPTIONS_CHOICE = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D')
    ]

    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_option = models.CharField(max_length=10, choices=OPTIONS_CHOICE)
