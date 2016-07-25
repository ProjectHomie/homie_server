from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    useremail = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    careate_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
