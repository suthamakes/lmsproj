from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    ModuleViewSet,
    ContentItemViewSet,
    QuizQuestionViewSet,
    EnrollmentViewSet
)


router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"modules", ModuleViewSet, basename="module")
router.register(r"content-items", ContentItemViewSet, basename="contentitem")
router.register(r"quiz-questions", QuizQuestionViewSet, basename="quizquestion")
router.register(r"enrollments", EnrollmentViewSet, basename="enrollment")

urlpatterns = [
    path("", include(router.urls)),
]
