from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^$', list, name="post-list"),
    url(r'^new/$', new, name="post-new"),
    url(r'^create/$', create, name="post-create"),
    url(r'^(?P<post_id>\d+)/$', detail, name="post-detail"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="post-edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="post-update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="post-delete"),
]
