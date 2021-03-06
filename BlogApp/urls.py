from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BlogApp.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
