from django.urls import path
from users import views


app_name = 'accounts'

urlpatterns = [
    path('', views.SignInView.as_view(), name="singin"),
    path('register/', views.SignUpView.as_view(), name="singup"),
    path('logout/', views.SignOutView.as_view(), name="singout")

]