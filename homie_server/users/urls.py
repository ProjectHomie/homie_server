from django.conf.urls import url

from users.views import *

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^my/page/$', mypage, name="mypage"),
]
