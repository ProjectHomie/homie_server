from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post


class PostListAPIView(APIView):

    def get(self, request, *args, **kwargs):

        data = [
            {
                "title": post.title,
                "content": post.content,
            }
            for post
            in Post.objects.all()
        ]

        return Response(data)
