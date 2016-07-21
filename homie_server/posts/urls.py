from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^$', list, name="post-list"),
    url(r'^(?P<post_id>\d+)/$', detail, name="post-detail"),
]
# url(r'^$', PostListView.as_view(), name="list"),
# url(r'^new/$', NewView.as_view(), name="new"),
# url(r'^create/$', PostCreateView.as_view(), name="create"),
# url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name="detail"),
# url(r'^(?P<post_id>\d+)/edit/$', EditView.as_view(), name="edit"),
# url(r'^(?P<post_id>\d+)/update/$', UpdateView.as_view(), name="update"),
# url(r'^(?P<post_id>\d+)/delete/$', DeleteView.as_view(), name="delete"),
