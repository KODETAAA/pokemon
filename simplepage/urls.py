from django.urls import path
from . import views

app_name = 'simplepage'

urlpatterns= [
	path('', views.Home.as_view(), name="home_view"),
	]