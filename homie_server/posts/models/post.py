from django.db import models
from django.core.urlresolvers import reverse
from users.models import User


class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()

    user = models.ForeignKey(User)

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

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

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "slug": self.hash_id,
            }
        )

    def get_update_url(self):
        return reverse(
            "posts:update",
            kwargs={
                "post_id": self.id,
            }
        )
