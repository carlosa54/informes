from django.views.generic import TemplateView
from django.contrib.auth import logout, authenticate

from django.shortcuts import redirect
from .models import User


def user_logout(request):
    logout(request)
    return redirect("/")
