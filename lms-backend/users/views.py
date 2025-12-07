from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, ILSResponse, LearningStyleScore, UserLog
from .serializers import (
    UserSerializer,
    ILSResponseSerializer,
    LearningStyleScoreSerializer,
    UserLogSerializer
)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ILSResponseViewSet(viewsets.ModelViewSet):
    queryset = ILSResponse.objects.all()
    serializer_class = ILSResponseSerializer


class ILSResponseSubmitView(APIView):
    """
    Handles submission of 44-question ILS responses as a single ArrayField per user.
    """

    def post(self, request):
        """
        Expected JSON:
        {
            "user_id": 1,
            "responses": ["a", "b", "a", ..., "b"]  # 44 items
        }
        """
        user_id = request.data.get("user_id")
        responses = request.data.get("responses")

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not responses or len(responses) != 44:
            return Response(
                {"error": f"Need exactly 44 responses, got {len(responses) if responses else 0}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": f"User {user_id} not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validate answers are 'a' or 'b'
        for ans in responses:
            if ans.lower() not in ('a', 'b'):
                return Response({"error": "Each answer must be 'a' or 'b'."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete old responses if user retakes
        ILSResponse.objects.filter(user=user).delete()

        # Save new response
        ils_response = ILSResponse.objects.create(
            user=user,
            answers=[a.lower() for a in responses]
        )

        # Calculate scores
        scores = self.calculate_scores(ils_response)

        # Save or update learning style score
        learning_style, _ = LearningStyleScore.objects.update_or_create(
            user=user,
            defaults=scores
        )

        serializer = LearningStyleScoreSerializer(learning_style)
        return Response({
            "message": "Success! Learning style calculated.",
            "scores": serializer.data
        }, status=status.HTTP_201_CREATED)

    def calculate_scores(self, ils_response):
        """
        Calculate learning style scores from the ArrayField using FSLSM mapping.
        """
        responses = ils_response.answers  # list of 44 answers

        # FSLSM dimension mapping (0-indexed)
        dimensions = {
            "active_reflective": (
                [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                "active_score",
                "reflective_score"
            ),
            "sensing_intuitive": (
                [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],
                "sensing_score",
                "intuitive_score"
            ),
            "visual_verbal": (
                [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42],
                "visual_score",
                "verbal_score"
            ),
            "sequential_global": (
                [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43],
                "sequential_score",
                "global_score"
            ),
        }

        results = {}
        for _, (indices, a_field, b_field) in dimensions.items():
            a_count = sum(1 for i in indices if responses[i] == 'a')
            b_count = sum(1 for i in indices if responses[i] == 'b')
            results[a_field] = a_count
            results[b_field] = b_count

        return results


class LearningStyleScoreViewSet(viewsets.ModelViewSet):
    queryset = LearningStyleScore.objects.all()
    serializer_class = LearningStyleScoreSerializer


class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer
