from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "users/mypage.html"
# class MypageView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             "users/mypage.html",
#             context={},
#         )
# @login_required
# def mypage(request):
#     return render(
#         request,
#         "users/mypage.html",
#         context={},
#     )
