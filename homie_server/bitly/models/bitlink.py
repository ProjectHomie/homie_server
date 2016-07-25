from users.models import User
from django.db import models


class Bitlink(models.Model):

    user = models.ForeignKey(User)

    original_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    careate_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url
