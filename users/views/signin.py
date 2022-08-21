from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from users.forms import LoginForm


class SignInView(View):
    template_name = 'users/account.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email_ = forms.cleaned_data["email"]
            password_ = forms.cleaned_data["password"]
            user = authenticate(email = email_, password = password_)

            if user:
                login(request, user)
                return redirect()
        context = {"form": forms}
        return render(request,self.template_name,context)