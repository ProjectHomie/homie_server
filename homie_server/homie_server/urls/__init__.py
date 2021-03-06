"""homie_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
    meView.as_view(), name="home"),
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from homie_server.views import *
# from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include("social.apps.django_app.urls", namespace="social")),
    url(r'^', include("users.urls", namespace="users")),
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^api/', include("homie_server.urls.api", namespace="api")),
    url(r'^$', HomeView.as_view(), name="home"),
]
