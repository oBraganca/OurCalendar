from django.urls import path, include
from ourcalendar import views


app_name = 'ourcalendar'

urlpatterns = [
    path("", views.TemplateView.as_view(), name="template"),
    path("addEvent/", views.create_event, name="newEvent"),
    path('account/',include('users.urls', namespace="users"))
]