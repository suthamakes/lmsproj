from django.db import models
# from courses.models import ContentItem


# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)  # email@student.ku.edu.np
    password = models.CharField(('password'), max_length=128)
    role = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='Student')  # user or teacher
    department = models.CharField(max_length=100, null=True)  # department necessary if user is teacher
    date_joined = models.DateField()
    first_sign_up = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"


class ILSResponse(models.Model):
    ANSWER_CHOICES = [
        ('a', 'A'),
        ('b', 'B')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_number = models.IntegerField()  # 1 to 44
    answer = models.CharField(max_length=2, choices=ANSWER_CHOICES)


class LearningStyleScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active_score = models.IntegerField()
    reflective_score = models.IntegerField()
    sensing_score = models.IntegerField()
    intuitive_score = models.IntegerField()
    visual_score = models.IntegerField()
    verbal_score = models.IntegerField()
    sequential_score = models.IntegerField()
    global_score = models.IntegerField()
    updated_at = models.DateField()

    def highest_score(self):
        scores = {
            "active": self.active_score,
            "reflective": self.reflective_score,
            "sensing": self.sensing_score,
            "intuitive": self.intuitive_score,
            "visual": self.visual_score,
            "verbal": self.verbal_score,
            "sequential": self.sequential_score,
            "global": self.global_score,
        }

        style = map(scores, key=scores.get)
        return style, scores[style]

    def __str__(self):
        return f"{self.user.username} : {self.highest_score(self)}"


class UserLog(models.Model):

    LEARNING_STYLE_CHOICES = [
        ('active', 'Active'),
        ('reflective', 'Reflective'),
        ('sensing', 'Sensing'),
        ('intuitive', 'Intuitive'),
        ('visual', 'Visual'),
        ('verbal', 'Verbal'),
        ('sequential', 'Sequential'),
        ('global', 'Global'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # content_id = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    content_id = models.ForeignKey("courses.ContentItem", on_delete=models.CASCADE)
    content_style_type = models.CharField(max_length=50, choices=LEARNING_STYLE_CHOICES)
    duration_seconds = models.IntegerField()
    completed = models.BooleanField(default=False)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.content.title}"
