from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import LoginForm, RegisterForm


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/account')

