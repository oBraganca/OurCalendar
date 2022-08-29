from django.views.generic import View
from django.shortcuts import render, redirect
from ourcalendar.models import Events, OurCalendar
from ourcalendar.forms import EventAdd


class TemplateView(View):
    template_name = 'template/calendar.html'

    def get(self, request, *args, **kwargs):
        
        forms = EventAdd

        calendar = OurCalendar.objects.filter(user=request.user)
        events = Events.objects.filter(calendar__in=calendar)
        
        event_list = []
        for event in events:
            event_list.append(
                {
                    "title": event.name,
                    "start": event.date_start.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.date_end.strftime("%Y-%m-%dT%H:%M:%S"),

                }
            )



        return render(request, self.template_name, {'form': forms, 'events':event_list})

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