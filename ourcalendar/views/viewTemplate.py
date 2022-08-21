from django.views.generic import View
from django.shortcuts import render, redirect


class TemplateView(View):
    template_name = 'template/template.html'

    def get(self, request, *args, **kwargs):
        context = {"": ""}
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