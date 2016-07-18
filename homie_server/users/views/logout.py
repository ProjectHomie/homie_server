from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("home"))
