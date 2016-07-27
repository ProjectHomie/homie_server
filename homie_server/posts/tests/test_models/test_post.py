from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostModelTastCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )

        self.post = self.post_set.create(
            title="test_title",
        )
