from rest_framework import serializers
from .models import User, ILSResponse, LearningStyleScore, UserLog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "role", "department",
            "date_joined", "first_sign_up"
        ]
        read_only_fields = ["id", "date_joined"]


class ILSResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ILSResponse
        fields = ["id", "user", "question_number", "answer"]
        read_only_fields = ["id"]


class LearningStyleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningStyleScore
        fields = [
            "id", "user", "active_score", "reflective_score", "sensing_score",
            "intuitive_score", "visual_score", "verbal_score", "sequential_score",
            "global_score", "updated_at"
        ]
        read_only_fields = ["id", "updated_at"]


class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = [
            "id", "user", "content_id", "content_style_type",
            "duration_seconds", "completed", "score"
        ]
        read_only_fields = ["id"]
