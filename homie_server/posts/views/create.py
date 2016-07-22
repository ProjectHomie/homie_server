from django.shortcuts import redirect

from posts.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    post = Post.objects.create(
        user=request.user,
        title=title,
        content=content,
    )

    return redirect(post)
