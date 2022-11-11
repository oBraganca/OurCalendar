
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.core import serializers


from users.forms import RegisterForm, LoginForm
from users.models import CustomUser
from ourcalendar.models import OurCalendar

import json

class SignUpView(View):
    template_name = 'users/account.html'
    form_class = LoginForm
    form_class2 = RegisterForm

    def post(self, request, *args, **kwargs):
        forms = self.form_class()
        forms2 = self.form_class2(request.POST)
        if forms2.is_valid():
            user = CustomUser.objects.create_user(
                first_name=forms2.cleaned_data["first_name"], 
                last_name=forms2.cleaned_data["last_name"], 
                email=forms2.cleaned_data["email"],
                password=forms2.cleaned_data["password"])
            
            OurCalendar.objects.create(user = user, qnt_merge = 0)

            return redirect('/account')
        
        request.session['forms2'] = request.POST
        request.session.modified = True
        
        return redirect('/account')