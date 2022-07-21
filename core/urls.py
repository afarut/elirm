from django.urls import path
from . import views


app_name = "core"

urlpatterns = [
	path('', views.index, name='index'),
	path('json', views.get_json, name='get_json'),	
]