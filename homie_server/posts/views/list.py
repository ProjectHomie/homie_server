from django.views.generic.list import ListView

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(is_public=True)
# def list(request):
#     page = request.GET.get("page", 1)
#     per = request.GET.get("per", 5)
#     paginator = Paginator(Post.objects.public(), per)
#     posts = paginator.page(page)
#     return render(
#         request,
#         "posts/list.html",
#         context={
#             "posts": posts,
#         },
#     )
