from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import redirect, render

from .base import PostBaseView


class PostCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )
# class PostCreateView(PostBaseView, CreateView):
#     fields = [
#         "title",
#         "content",
#     ]
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         # return super(PostCreateView, self).form_valid(form)
#         return super(new, self).form_valid(form)


class PostCreateConfirmView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("posts:create"))
    
    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")

        return render(
            request,
            "posts/confirm.html",
            context={
                "title": title,
                "content": content,
            },
        )
#     def post(self, request, *arg, **kwargs):
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         post = Post.objects.create(
#             user=request.user,
#             title=title,
#             content=content,
#         )
#         return redirect(post)
