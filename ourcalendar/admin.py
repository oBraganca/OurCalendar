

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Events, OurCalendar

admin.site.register(Events)
admin.site.register(OurCalendar)
