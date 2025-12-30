# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import Course, Module, ContentItem, QuizQuestion, Enrollment
from .serializers import (
    CourseSerializer,
    ModuleSerializer,
    ContentItemSerializer,
    QuizQuestionSerializer,
    EnrollmentSerializer
)
from rest_framework.response import Response
from .permissions import IsTeacher, IsOwnerTeacher, IsStudent
# from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Course.objects.none()

        if user.role == "teacher":
            return Course.objects.filter(created_by=user)

        if user.role == "student":
            return Course.objects.filter(
                enrollments__student=user,
                enrollments__is_active=True
            )

        return Course.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsTeacher()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerTeacher()]
        return []

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "teacher":
            return Module.objects.filter(course__created_by=user)

        if user.role == "student":
            return Module.objects.filter(
                course__enrollments__student=user,
                course__enrollments__is_active=True
            )

        return Module.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsTeacher()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerTeacher()]
        return []

    def perform_create(self, serializer):
        course = serializer.validated_data["course"]

        if course.created_by != self.request.user:
            raise PermissionDenied("You do not own this course.")

        serializer.save(created_by=self.request.user)


class ContentItemViewSet(viewsets.ModelViewSet):
    serializer_class = ContentItemSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "teacher":
            return ContentItem.objects.filter(
                module__course__created_by=user
            )

        if user.role == "student":
            return ContentItem.objects.filter(
                module__course__enrollments__student=user,
                module__course__enrollments__is_active=True
            )

        return ContentItem.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsTeacher()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerTeacher()]
        return []

    def perform_create(self, serializer):
        module = serializer.validated_data["module"]

        if module.course.created_by != self.request.user:
            raise PermissionDenied("You do not own this course.")

        serializer.save(created_by=self.request.user)


class QuizQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "teacher":
            return QuizQuestion.objects.filter(
                content_item__module__course__created_by=user
            )

        if user.role == "student":
            return QuizQuestion.objects.filter(
                content_item__module__course__enrollments__student=user,
                content_item__module__course__enrollments__is_active=True
            )

        return QuizQuestion.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsTeacher()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerTeacher()]
        return []


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudent]

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

    def create(self, request, *args, **kwargs):
        course_id = request.data.get("course")

        if not course_id:
            raise ValidationError("course is required")

        course = Course.objects.filter(id=course_id).first()
        if not course:
            raise ValidationError("Invalid course")

        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )

        if not created:
            raise ValidationError("Already enrolled in this course")

        serializer = self.get_serializer(enrollment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
