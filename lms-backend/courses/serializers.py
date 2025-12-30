from rest_framework import serializers
from django.utils import timezone
from .models import Course, Module, ContentItem, QuizQuestion
from users.serializers import UserSerializer
from .models import Enrollment


class CourseSerializer(serializers.ModelSerializer):
    course_created_by = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(
        default=serializers.CreateOnlyDefault(timezone.now)
    )

    class Meta:
        model = Course
        fields = ["id", "title", "description", "course_created_by", "created_at"]
        read_only_fields = ["id", "created_at", 'course_created_by']


class ModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    module_created_by = UserSerializer(read_only=True)

    class Meta:
        model = Module
        fields = ["id", "course", "title", "module_created_by", "order_number"]
        read_only_fields = ["id", "module_created_by"]


class ContentItemSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)
    content_created_by = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(
        default=serializers.CreateOnlyDefault(timezone.now)
    )

    class Meta:
        model = ContentItem
        fields = [
            "id", "module", "title", "content_type", "content_created_by",
            "data", "file_url", "learning_style_type", "difficulty_level", "created_at"
        ]
        read_only_fields = ["id", "created_at", "content_created_by"]


class QuizQuestionSerializer(serializers.ModelSerializer):
    content_item = ContentItemSerializer(read_only=True)

    class Meta:
        model = QuizQuestion
        fields = [
            "id", "content_item", "question", "option_a", "option_b",
            "option_c", "option_d", "correct_option"
        ]
        read_only_fields = ["id"]


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.ReadOnlyField(source="course.title")

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "course",
            "course_title",
            "enrolled_at",
            "expires_at",
            "is_active",
        ]
        read_only_fields = ["enrolled_at"]
