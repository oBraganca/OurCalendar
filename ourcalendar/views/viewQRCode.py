from django.views.generic import View
from django.shortcuts import render, redirect
from ourcalendar.models import Events, OurCalendar
from ourcalendar.forms import EventAdd, MergeEvents
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from io import BytesIO

import qrcode
import qrcode.image.svg



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
        img = qrcode.make(request.META['HTTP_HOST']+"/mergeCalendar/{0}/".format(list(idC)[0]), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)

        context = {'svg': stream.getvalue().decode(), 'user_info':user_, "pictureProfile":picture_profile}

        return render(request, self.template_name, context)

class MergeCalendar(LoginRequiredMixin, View):
    template_name = 'template/mergeCalendar.html'
    form_class = MergeEvents

    login_url = '/account/'

    def get(self, request, *args, **kwargs):
        user_ = CustomUser.objects.get(email=request.user)
        picture_profile = user_.first_name[0]        

        calendar_ = OurCalendar.objects.get(id=kwargs.get('id'))

        instence_data = {"de":str(calendar_.user), "calendario_id":kwargs.get('id')}

        forms = MergeEvents(initial=instence_data)
        forms.fields['de'].widget.attrs['disabled'] = True
        forms.fields['calendario_id'].widget.attrs['disabled'] = True

        context = {'form': forms, 'user_info':user_, "pictureProfile":picture_profile}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email_ = forms.cleaned_data["de"]
            calendario_id = forms.cleaned_data["calendario_id"]
            events = Events.objects.filter(calendar__in=calendario_id)

            calendar = OurCalendar.objects.get(user = request.user)
            for event in events:
                # eventTest = Events.objects.filter(calendar__in=str(calendar.id), date_end__gte=datetime.datetime.now()).exclude(unic_code = event.unic_code)
                eventTest = Events.objects.filter(calendar__in=str(calendar.id), unic_code = event.unic_code)        
                if not eventTest:
                    Events.objects.create(name=event.name, description=event.description, date_start = event.date_start, date_end = event.date_end, calendar = calendar, origim = event.origim, unic_code=event.unic_code)

        return redirect('/')

