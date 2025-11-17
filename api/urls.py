from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    SkillViewSet,
    ProjectViewSet,
    ConnectionViewSet,
    MessageViewSet,
    EndorsementViewSet,
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'connections', ConnectionViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'endorsements', EndorsementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
