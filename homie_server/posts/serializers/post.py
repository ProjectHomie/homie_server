from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username",)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",

            "username",
        ]
