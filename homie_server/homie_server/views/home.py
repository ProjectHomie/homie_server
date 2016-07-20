from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from django.views.generic import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "home.html",
            context={},
        )
