from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context["site_name"] = "homie"
        return context
