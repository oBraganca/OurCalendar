from django import forms
from django.forms import DateInput, ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Events
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
import datetime

ACCESS = (
    ('PB', 'Public'),
    ('PV', 'Private')
)

class EventAdd(ModelForm):
    class Meta:
        model = Events
        fields = ["name", "description", "date_start", "date_end", "access"]
        labels = {
            'name': _('Title'),
            'description': _('Description'),
            'date_start': _('Start'),
            'date_end': _('End'),
            'access': _('Access'),
        }
        # datetime-local is a HTML5 input type
        
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control w-100 mb-3", "placeholder": "Nome do Evento"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Descrição do Evento",
                }
            ),
            "date_start": DateInput(
                attrs={"type": "datetime-local", "class": "form-control mb-3", 'min': datetime.datetime.now()}
            ),
            "date_end": DateInput(
                attrs={"type": "datetime-local", "class": "form-control mb-3","required":True,}
            ),
        }
        access = forms.ChoiceField(choices=ACCESS)
        
    # def clean(self):
    #     date_start = self.cleaned_data.get("date_start")
    #     date_end = self.cleaned_data.get("date_end")
    #     if date_start < datetime.datetime.now():
    #         raise ValidationError("Já existe uma conta com esse email.")
    #     if date_end < datetime.datetime.now():
    #         raise ValidationError("As senhas não são iguais, tente novamente.")
        
        
    #     return password2

class MergeEvents(forms.Form):
    de = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'recipient-name'}))
    calendario_id = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control', 'id':'recipient-name'}))
    

class GenerateCode(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'code-calendar'}))
    

class SendMergeCalendar(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'recipient-name'}))
class SolicitFollow(forms.Form):
    code_user = forms.CharField(widget=forms.TextInput(attrs={'type':'email','class': 'form-control ', 'id':'solicit-follow', "placeholder":"email@mail.com"}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code_user'].label = ""