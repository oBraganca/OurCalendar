from django.views.generic import View
from django.shortcuts import render, redirect
from ourcalendar.models import Events, OurCalendar
from ourcalendar.forms import EventAdd
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout

class TemplateView(LoginRequiredMixin, View):
    template_name = 'template/calendar.html'


    login_url = '/account/'


    def get(self, request, *args, **kwargs):
        
        forms = EventAdd()

        calendar = OurCalendar.objects.filter(user=request.user)
        events = Events.objects.filter(calendar__in=calendar)

        user_ = CustomUser.objects.get(email=request.user)
        picture_profile = user_.first_name[0]        

        event_list = []
        for event in events:
            event_list.append(
                {
                    "title": event.name,
                    "start": event.date_start.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.date_end.strftime("%Y-%m-%dT%H:%M:%S"),

                }
            )

        context = {'form': forms, 'events':event_list, 'user_info':user_, "pictureProfile":picture_profile, "domain":request.META['HTTP_HOST']}

        return render(request, self.template_name, context)

@login_required
def create_event(request):
    form = EventAdd(request.POST or None)

    if request.POST and form.is_valid():
        title = form.cleaned_data["name"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["date_start"]
        end_time = form.cleaned_data["date_end"]
        calendar = OurCalendar.objects.get(user=request.user)

        Events.objects.create(
            name=title,
            description=description,
            date_start=start_time,
            date_end=end_time,
            calendar=calendar,
            origim=calendar,

        )
        return HttpResponseRedirect(reverse("ourcalendar:template"))
    return HttpResponseRedirect(reverse("ourcalendar:template"))