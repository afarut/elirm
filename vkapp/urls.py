from django.urls import path
from . import views


app_name = "vkapp"

urlpatterns = [
	path('', views.vk_bot, name='vk_bot'),
]