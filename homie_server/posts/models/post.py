from django.db import models
from django.core.urlresolvers import reverse


# class PostManager(models.Manager):
#     def public(self):
#         return self.filter(is_public=True)
class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )

    content = models.TextField()
    is_public = models.BooleanField(
        default=True,
    )

    careate_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
#     def get_absolute_url(self):
#         return reverse(
#             "post:detail",
#             kwargs={
#                 "pk": self.id,
#             },
#         )
#     def get_update_url(self):
#         return reverse(
#             "posts:update",
#             kwargs={
#                 "post_id": self.id,
#             }
#         )
