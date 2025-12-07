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


class LearningStyleScoreViewSet(viewsets.ModelViewSet):
    queryset = LearningStyleScore.objects.all()
    serializer_class = LearningStyleScoreSerializer


class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer
