from django.urls import path
from ngo import views

app_name = "ngo"

urlpatterns = [
    path('signup', views.signup, name='signup'),
]
