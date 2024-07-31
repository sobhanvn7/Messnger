# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet, AuthView

app_name = 'api'
urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]

router = SimpleRouter()
router.register('user', UserViewSet),
router.register('chat', ChatViewSet),
urlpatterns += router.urls
