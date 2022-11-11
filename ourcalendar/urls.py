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
    # path('account/',include('users.urls', namespace="users")),
    path('mergeCalendar/<int:id>',views.MergeCalendar.as_view(), name="template"),
    path("mergedCalendar/", views.MergeCalendar.as_view(), name="newEvent"),
    path("getForm/", views.EventAjax.getForm),
    path("getInfo/", views.EventAjax.getInfo),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    path("excludeEvent/", views.EventAjax.excludeEvent)
]