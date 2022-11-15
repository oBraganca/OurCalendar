from django.views.generic import View
from django.shortcuts import render
from ourcalendar.models import Events, OurCalendar, CalendarFollow
from ourcalendar.forms import EventAdd
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from users.models import CustomUser
class TemplateView(LoginRequiredMixin, View):
    template_name = 'template/calendar.html'
    id = None

    login_url = '/account/'


    def get(self, request, *args, **kwargs):
        
        forms = EventAdd()
        
        user_ = CustomUser.objects.get(email=request.user)
        calendar = OurCalendar.objects.get(user=request.user)
        
        self.id = calendar.id
        
        users = CalendarFollow.objects.all().prefetch_related("follower").filter(calendar = calendar).order_by('id')[:2]
        
        users_list = []
        
        users_list.append({
                    "first_name": user_.first_name,
                    "last_name": user_.last_name,
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
            
        events = Events.objects.filter(calendar=calendar)
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

        context = {'form': forms, 'events':event_list, 'user_info':user_, 
                   "pictureProfile":picture_profile, "domain":request.META['HTTP_HOST'], 
                   "idC":self.id, "main":True, "belongs":"Meu Calendario", "users":users_list}

        return render(request, self.template_name, context)
    
    
class TemplateViewFollow(LoginRequiredMixin, View):
    template_name = 'template/calendar.html'
    id = None

    login_url = '/account/'


    def get(self, request, *args, **kwargs):
        
        forms = EventAdd()
        
        
        
        
        
        self.id = self.kwargs.get("id")

        calendar = OurCalendar.objects.get(id=self.id)
        events = Events.objects.filter(calendar=calendar)
        
        
        users = CalendarFollow.objects.all().prefetch_related("follower").filter(calendar = calendar).order_by('id')[:2]
        user_main = CustomUser.objects.get(email = calendar.user.email) 
        
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

        context = {'form': forms, 'events':event_list, 'user_info':user_, 
                   "pictureProfile":picture_profile, "domain":request.META['HTTP_HOST'], 
                   "idC":self.id, "belongs":calendar.name, "users":users_list}

        return render(request, self.template_name, context)
    

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

def edit_event(request):
    form = EventAdd(request.POST)

    if request.POST and form.is_valid():
        unic_code = request.POST.get("code")
        id = request.POST.get("id")
        
        title = form.cleaned_data["name"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["date_start"]
        end_time = form.cleaned_data["date_end"]

        Events.objects.filter(
            id = id,
            unic_code = unic_code 
        ).update(
            name=title,
            description=description,
            date_start=start_time,
            date_end=end_time,
            
        )
        
        return HttpResponseRedirect(reverse("ourcalendar:template"))
    return HttpResponseRedirect(reverse("ourcalendar:template"))