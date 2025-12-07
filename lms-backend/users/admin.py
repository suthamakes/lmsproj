from django.contrib import admin
from .models import User, LearningStyleScore, ILSResponse, UserLog

# Register your models here.

admin.site.register(User)
admin.site.register(UserLog)
admin.site.register(LearningStyleScore)
admin.site.register(ILSResponse)
