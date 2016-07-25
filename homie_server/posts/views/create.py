from django.views.generic import View
from django.shortcuts import redirect

from posts.models import Post


class PostCreateView(View):

    def post(self, request, *arg, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")

        post = Post.objects.create(
            user=request.user,
            title=title,
            content=content,
        )

        return redirect(post)
