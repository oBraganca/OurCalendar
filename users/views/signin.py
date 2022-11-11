from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import LoginForm, RegisterForm


class SignInView(View):
    template_name = 'users/account.html'
    form_class = LoginForm
    form_class2 = RegisterForm
    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        forms2 = self.form_class2()
        if 'forms2' in request.session:
            forms2 = self.form_class2(request.session['forms2'])
            del request.session['forms2']
        context = {"form": forms, "form2": forms2}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        forms2 = self.form_class2()
        if forms.is_valid():
            email_ = forms.cleaned_data["email"]
            password_ = forms.cleaned_data["password"]

            user = authenticate(email = email_, password = password_)
            if user is not None:
                login(request, user)
                return redirect("ourcalendar:template")

        context = {"form": forms, "form2": forms2}
        return render(request,self.template_name,context)

