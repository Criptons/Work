from rest_framework import serializers
from .models import Post, Comment, Vote


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class VoteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = "__all__"


class PostSerializers(serializers.ModelSerializer):
    post_comment = CommentSerializers(many=True, required=False, allow_null=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'link',
            'amount_votes',
            'author',
            'date_created',
            'post_comment'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True}
        }
