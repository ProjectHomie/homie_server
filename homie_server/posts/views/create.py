from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import redirect, render
from .base import PostBaseView
from django.contrib.auth import get_user_model


class PostCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")

        # post = get_user_model().post_set.create(
        post = request.user.post_set.create(
            title=title,
            content=content,
        )

        return redirect(reverse("posts:create"))
# class PostCreateView(PostBaseView, CreateView):
#     fields = [
#         "title",
#         "content",
#     ]
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         # return super(PostCreateView, self).form_valid(form)
#         return super(new, self).form_valid(form)


class PostCreateConfirmView(LoginRequiredMixin, View):

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
