
from django.views.generic import View
from django.shortcuts import render
from ourcalendar.models import Events, OurCalendar
from ourcalendar.forms import EventAdd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from users.models import CustomUser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django import forms

import datetime

class TemplateDashboard(LoginRequiredMixin, View):
    template_name = 'template/dashboard.html'


    login_url = '/account/'

    def get(self, request, *args, **kwargs):
        
        forms = EventAdd()

        calendar = OurCalendar.objects.get(user=request.user)
        qnt_events = len(Events.objects.filter(calendar=calendar, date_end__gte=datetime.datetime.now()))
        qnt_end = len(Events.objects.filter(calendar=calendar, date_end__lte=datetime.datetime.now()))
        events = Events.objects.filter(calendar=calendar)

        user_ = CustomUser.objects.get(email=request.user)
        picture_profile = user_.first_name[0]

        context = {
                    'user_info':user_, 
                    "pictureProfile":picture_profile, 
                    'merged':calendar.qnt_merge, 
                    'active':qnt_events, 
                    'ending':qnt_end, 
                    'events': events
                    }

        return render(request, self.template_name, context)

class EventAjax(View):
    template_name = 'templates/dashboard.html'
    
    @classmethod
    @method_decorator(ensure_csrf_cookie)
    def excludeEvent(self, request, *args, **kwargs):
        id = request.POST.get('id')
        calendar = OurCalendar.objects.get(user=request.user)
        print(Events.objects.filter(id=id,calendar=calendar).delete())
        
        response_data = {"status": "success"}
        
        return JsonResponse(response_data)
        
    
    @classmethod
    @method_decorator(ensure_csrf_cookie)
    def getInfo(self, request, *args, **kwargs):
        id = request.POST.get('id')
        calendar = OurCalendar.objects.get(user=request.user)
        event = Events.objects.get(id=id,calendar=calendar)
        
        response_data =  {"event_name": event.name, 'event_date_start': event.date_start, 'event_date_end':event.date_end, "description": event.description, "event_id":id}
        
        return JsonResponse(response_data)
        
    @classmethod
    @method_decorator(ensure_csrf_cookie)
    def getForm(self, request, *args, **kwargs):
        id = request.POST.get('id')
        calendar = OurCalendar.objects.get(user=request.user)
        forms = EventAdd()
        event = Events.objects.get(id=id,calendar=calendar)
        
        forms = self.setForm(forms, event)
        
        return HttpResponse(forms.as_p())
    
    @staticmethod
    def setForm(form, event):
        form.fields["name"].initial = event.name
        form.fields["description"].initial = event.description
        form.fields["date_start"].initial = (event.date_start.strftime("%Y-%m-%d %H:%M:%S"))
        form.fields["date_end"].initial = (event.date_end.strftime("%Y-%m-%d %H:%M:%S"))
        form.fields["access"].initial = event.access
        
        form.fields['id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=event.id)
        form.fields['code'] = forms.IntegerField(widget=forms.HiddenInput(), initial=event.unic_code)
        
        return form