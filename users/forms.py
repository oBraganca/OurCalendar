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
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"firstlogname", 'class':"form-style", 'placeholder':"Nome", 'id':"firtslogname", 'autocomplete':"off"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"lastlogname", 'class':"form-style", 'placeholder':"Sobrenome", 'id':"lastlogname", 'autocomplete':"off"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={ 'name':"confirmPassword", 'class':"form-style", 'placeholder':"Confirme a Senha", 'id':"confirmLogpass", 'autocomplete':"off"}))
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirmPassword")
        if password and confirmPassword and password != confirmPassword:
            raise ValidationError("As senhas não são iguais, tente novamente.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return 