

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Events, OurCalendar, CalendarFollow, RequestCalendarFollow

admin.site.register(Events)
admin.site.register(OurCalendar)
admin.site.register(CalendarFollow)
admin.site.register(RequestCalendarFollow)
