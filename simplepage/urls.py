from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'simplepage'

urlpatterns= [
	path('', views.Home.as_view(), name="home_view"),
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)