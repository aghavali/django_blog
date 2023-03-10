from rest_framework import serializers
from .models import Post, Upvote, Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'updated', 'user', 'upvote_count')

class UpvoteSerializer(serializers.Serializer):
    class Meta:
        model = Upvote
        field = ('id', 'user', 'post')

class CommentSerializers(serializers.Serializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'body', 'created')