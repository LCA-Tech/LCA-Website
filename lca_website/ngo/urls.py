from django.urls import path
from ngo import views

app_name = "ngo"

urlpatterns = [
    path('ngohome', views.NgoListView.as_view(), name='list'),
    path('signup', views.signup, name='signup'),
    path('<int:pk>', views.NgoDetailView.as_view(), name='ngo'),
    path('<id>/results/', views.results, name='results'),
    path('<id>/', views.detail, name='detail'),
    path('', views.homepage, name='homepage'),

]
