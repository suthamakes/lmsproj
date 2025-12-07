from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ILSResponseSubmitView,
    ILSResponseViewSet,
    LearningStyleScoreViewSet,
    UserLogViewSet
)


router = DefaultRouter()
router.register("users", UserViewSet)

router.register("ils-responses", ILSResponseViewSet)
# router.register() only accepts ViewSets, not APIViews
router.register("learning-style-scores", LearningStyleScoreViewSet)
router.register("logs", UserLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/ils/submit/", ILSResponseSubmitView.as_view(), name="ils-submit"),
]
