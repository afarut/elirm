from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vk/', include("vkapp.urls")),
    path('tools/', include("tools.urls")),
    path('', include("core.urls"))
]
