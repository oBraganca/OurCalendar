from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"firstlogname", 'class':"form-style", 'placeholder':"Nome", 'id':"firtslogname", 'autocomplete':"off"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"lastlogname", 'class':"form-style", 'placeholder':"Sobrenome", 'id':"lastlogname", 'autocomplete':"off"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"confirmPassword", 'class':"form-style", 'placeholder':"Confirme a Senha", 'id':"confirmLogpass", 'autocomplete':"off"}))
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')

        if password != confirmPassword:
            raise forms.ValidationError("As senhas difitadas não são iguais")
