from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .base import PostBaseView


class PostCreateView(PostBaseView, CreateView):
    fields = [
        "title",
        "content",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
#     def post(self, request, *arg, **kwargs):
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         post = Post.objects.create(
#             user=request.user,
#             title=title,
#             content=content,
#         )
#         return redirect(post)
