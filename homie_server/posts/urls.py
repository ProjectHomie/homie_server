from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', PostCreateView.as_view(), name="create"),
    url(r'^confirm/$', PostCreateConfirmView.as_view(), name="confirm"),
    url(r'^(?P<slug>\w+)/$', PostDetailView.as_view(), name="detail"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),
]
