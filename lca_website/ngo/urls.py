from django.conf.urls import url
from ngo import views

app_name = "ngo"

urlpatterns = [
    url(r"^ngo/signup", views.ngo_signup, name="ngo_signup"),
]
