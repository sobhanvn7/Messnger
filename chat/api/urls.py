# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet, AuthView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('', include(router.urls)),
]
