# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Course, Module, ContentItem, QuizQuestion
from .serializers import (
    CourseSerializer,
    ModuleSerializer,
    ContentItemSerializer,
    QuizQuestionSerializer
)
from .permissions import IsTeacher, IsOwnerTeacher
# from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsTeacher()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerTeacher()]
        return []

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in.")

        if user.role != "teacher":
            raise PermissionDenied("Only teacher can create modules.")

        course_id = self.request.data.get("course")
        if course_id is None:
            raise PermissionDenied("course field is required.")

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise PermissionDenied("Invalid course.")

        serializer.save(module_created_by=user, course=course)


class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("Login required.")

        if user.role != "teacher":
            raise PermissionDenied("Only teachers can add content.")

        module_id = self.request.data.get("module")
        if module_id is None:
            raise PermissionDenied("module field is required.")

        try:
            module = Module.objects.get(id=module_id)
        except Module.DoesNotExist:
            raise PermissionDenied("Invalid module.")

        serializer.save(content_created_by=user, module=module)


class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("Login required.")

        if user.role != "teacher":
            raise PermissionDenied("Only teachers can create quiz questions.")

        content_item_id = self.request.data.get("content_item")

        if not content_item_id:
            raise PermissionDenied("content_item field is required.")

        try:
            content_item = ContentItem.objects.get(id=content_item_id)
        except ContentItem.DoesNotExist:
            raise PermissionDenied("Invalid ContentItem ID.")

        serializer.save(content_item=content_item)
