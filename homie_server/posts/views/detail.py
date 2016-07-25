from django.views.generic.detail import DetailView

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
# def detail(request, post_id):
#     return render(
#         request,
#         "posts/detail.html",
#         context={
#             "post": Post.objects.get(id=post_id),
#         },
#     )
