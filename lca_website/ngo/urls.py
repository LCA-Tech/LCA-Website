from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = "ngo"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^ngo/signup", views.ngo_signup, name="ngo_signup"),
    path('<name>/results/', views.results, name='results'),
    path('<name>/', views.detail, name='detail'),

]
