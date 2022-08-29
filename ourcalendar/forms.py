from django import forms
from .models import Events

class EventAdd(forms.Form):
    name_event = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'name':"firstlogname", 'class':"form-style", 'placeholder':"Nome", 'id':"firtslogname", 'autocomplete':"off"}))
    description = forms.CharField(widget=forms.TextInput(attrs={'name':"lastlogname", 'class':"form-style", 'placeholder':"Sobrenome", 'id':"lastlogname", 'autocomplete':"off"}))
    date_start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'name':'logemails','class': 'form-style', 'placeholder': 'Digite seu E-mail', 'id':'logemail', 'autocomplete': 'off'}))
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={ 'name':"logpass", 'class':"form-style", 'placeholder':"Digite a Senha", 'id':"logpass", 'autocomplete':"off"}))
