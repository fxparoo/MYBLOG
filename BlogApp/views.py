from rest_framework import viewsets, status
from rest_framework.response import Response
from BlogApp.models import Post, Comment
from BlogApp.serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def all_post(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
