from django.contrib import admin

from posts.models import Post
from users.models import User


admin.site.register(Post)
admin.site.register(User)
