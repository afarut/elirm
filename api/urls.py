from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
	path('', views.index, name='index'),
	path('json/', views.get_json, name='get_json'),	
] 
