from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BlogApp.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('Post', PostViewSet, basename='post')
router.register('Comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
