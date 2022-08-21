from django.urls import path, include
from ourcalendar import views


app_name = 'users'

urlpatterns = [
    path("", views.TemplateView.as_view(), name="template"),
    path('account/',include('users.urls', namespace="users"))
]