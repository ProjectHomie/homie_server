from django.views.generic.detail import DetailView

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
    slug_field = "hash_id"
#         request,
#         "posts/detail.html",
#         context={
#             "post": Post.objects.get(id=post_id),
#         },
#     )
