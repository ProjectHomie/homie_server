from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<post_id>\d+)/$', detail, name="detail"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),
]
