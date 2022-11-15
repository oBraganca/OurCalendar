from django import forms
from django.forms import DateInput, ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Events
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField, Div, Row, Column

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
                attrs={"type": "datetime-local", "class": "form-control mb-3"}
            ),
            "date_end": DateInput(
                attrs={"type": "datetime-local", "class": "form-control mb-3"}
            ),
        }
        access = forms.ChoiceField(choices=ACCESS)

class MergeEvents(forms.Form):
    de = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'recipient-name'}))
    calendario_id = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control', 'id':'recipient-name'}))
    

class GenerateCode(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'code-calendar'}))
    

class SendMergeCalendar(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class': 'form-control mb-3', 'id':'recipient-name'}))