from rest_framework import viewsets, response
from .models import Post, Comment, Vote
from .serializers import PostSerializers, CommentSerializers, VoteSerializers


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_isLiked(self, obj):
        requestUser = self.context['request'].user
        return Vote.objects.filter(post=obj, liker=requestUser).exists()


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class VoteModelViewSet(viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializers

    def create(self, request):
        user = request.user
        serializer = VoteSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)