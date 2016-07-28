from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import redirect, render
from .base import PostBaseView

   
class PostCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )

    def post(tself, request, *args, **kwargs):

        title = request.POST.get("title")
        content = request.POST.get("content")
        post = request.user.post_set.create(
            title=title,
            content=content,
        )
        return redirect(reverse("posts:create"))

        
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
