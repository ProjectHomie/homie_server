from django.shortcuts import render

from posts.models import Post


def detail(request, post_id):
    return render(
        request,
        "posts/detail.html",
        context={
            "post": Post.objects.get(id=post_id),
        },
    )
