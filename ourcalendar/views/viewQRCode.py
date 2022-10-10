from django.views.generic import View
from django.shortcuts import render, redirect
from ourcalendar.models import Events, OurCalendar
from ourcalendar.forms import EventAdd
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from users.models import CustomUser
import qrcode
import qrcode.image.svg
from io import BytesIO

class TemplateQR(LoginRequiredMixin, View):
    template_name = 'template/calendarQR.html'


    login_url = '/account/'

    def get(self, request, *args, **kwargs):
        
        forms = EventAdd()

        calendar = OurCalendar.objects.filter(user=request.user)
        idC=calendar.values_list('pk',flat=True)
        events = Events.objects.filter(calendar__in=calendar)

        user_ = CustomUser.objects.get(email=request.user)
        picture_profile = user_.first_name[0]        


        factory = qrcode.image.svg.SvgImage
        img = qrcode.make("https://www.instagram.com/{0}/".format(list(idC)[0]), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)

        context = {'svg': stream.getvalue().decode()}

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