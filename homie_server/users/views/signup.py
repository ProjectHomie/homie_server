from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, redirect


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        phonenumber = request.POST.get("phonenumber")
        useremail = request.POST.get("username")
        address = request.POST.get("address")

        # TODO: validateions (username)

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            phonenumber=phonenumber,
            useremail=useremail,
            address=address,
        )

        # TODO:flash messages( success, error messages)
        return redirect(reverse("home"))
