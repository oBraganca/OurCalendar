from django.urls import path, include
from ourcalendar import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


app_name = 'ourcalendar'

urlpatterns = [
    path("", views.TemplateView.as_view(), name="template"),
    path("share/", views.TemplateQR.as_view(), name='share'),
    path("dashboard/", views.TemplateDashboard.as_view(), name='dashboard'),
    path("addEvent/", views.create_event, name="newEvent"),
    path("editEvent/", views.edit_event, name="newEvent"),
    path("all-calendars/", views.ListTemplateView.as_view(), name="calendars"),
    path("all-calendars/<int:id>", views.TemplateViewFollow.as_view(), name="calendar-follow"),
    path('mergeCalendar/<int:id>',views.MergeCalendar.as_view(), name="template"),
    path("mergedCalendar/", views.MergeCalendar.as_view(), name="newEvent"),
    
    path("getForm/", views.EventAjax.getForm),
    path("getInfo/", views.EventAjax.getInfo),
    path("getCodeMerge/", views.EventAjax.getCode),
    path("getUseCoder/", views.EventAjax.getFormCode),
    path("mergeUseCode/", views.EventAjax.postFormCode),
    
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    path("excludeEvent/", views.EventAjax.excludeEvent)
]