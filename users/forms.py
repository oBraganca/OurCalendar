import email
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise ValidationError("Desculpe, mas algo no login deu errado, tente novamente.")
        return self.cleaned_data
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"firstlogname", 'class':"form-style", 'placeholder':"Nome", 'id':"firtslogname", 'autocomplete':"off"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"lastlogname", 'class':"form-style", 'placeholder':"Sobrenome", 'id':"lastlogname", 'autocomplete':"off"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"confirmPassword", 'class':"form-style", 'placeholder':"Confirme a Senha", 'id':"confirmLogpass", 'autocomplete':"off"}))
    
    def clean(self):
        errors = []
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirmPassword")
        if password1 and password2 and password1 != password2:
            errors.append(ValidationError("As senhas não são iguais, tente novamente."))
            
        if errors:
            raise ValidationError("As senhas não são iguais, tente novamente.")
        
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return 