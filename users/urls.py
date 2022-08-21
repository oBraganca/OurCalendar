from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('', views.SignInView.as_view(), name="singin")

]