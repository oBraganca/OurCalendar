from django.views.generic import View
from django.shortcuts import render
from ourcalendar.models import Events, OurCalendar, CalendarFollow
from ourcalendar.forms import EventAdd
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from users.models import CustomUser

class ListTemplateView(LoginRequiredMixin, View):
    template_name = 'template/calendarios.html'


    login_url = '/account/'


    def get(self, request, *args, **kwargs):
        
        
        calendars_queryset = CalendarFollow.objects.filter(follower = request.user)
        calendars = OurCalendar.objects.filter(calendarfollow__in = calendars_queryset)
        
        
        calendar = OurCalendar.objects.get(user=request.user)
        
        users = CalendarFollow.objects.all().prefetch_related("follower").filter(calendar = calendar).order_by('id')[:2]
        user_main = CustomUser.objects.get(email = calendar.user.email) 
        
        calendar_list = []
        for calendar in calendars:
            calendar_list.append(
                {
                    "title": calendar.name,
                    "belongs": calendar.user.email,
                    "id": calendar.id,
                }
            )
        
        user_ = CustomUser.objects.get(email=request.user)
        picture_profile = user_.first_name[0]        

        users_list = []
        users_list.append({
                    "first_name": user_main.first_name,
                    "last_name": user_main.last_name,
                    "main": True,
                    })

        for user in users:
            users_list.append(
                {
                    "first_name": user.follower.first_name,
                    "last_name": user.follower.last_name,
                    "merged": user.qnt_merge,

                }
            )

        context = {'calendar_list': calendar_list, 'user_info':user_, "pictureProfile":picture_profile, "domain":request.META['HTTP_HOST'], "belongs":"Meu Calendario", "users":users_list}

        return render(request, self.template_name, context)
    
    