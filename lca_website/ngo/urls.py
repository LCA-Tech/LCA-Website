from django.urls import path
from ngo import views

app_name = "ngo"

urlpatterns = [
    path('', views.NgoListView.as_view(), name='list'),
    path('signup', views.signup, name='signup'),
    path('<int:pk>', views.NgoDetailView.as_view(), name='ngo'),
]
