from django.urls import path
from . import views

urlpatterns  = [
    path('',views.home, name="home"),
    path('take_date', views.take_date, name='take_date'),
] 