from django.views.generic.list import View

from posts.models import Post


class PostBaseView(View):
    model = Post
