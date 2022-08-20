from django.urls import path
from . import views


app_name = "tools"

urlpatterns = [
	path('', views.index, name='index'),
	path('convertor/audio', views.audio_convertor, name='audio_convertor'),
	path('convertor/image', views.image_convertor, name='image_convertor'),
	path('chat', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]