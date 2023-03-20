from django.urls import path
from apps.settings.views import index,video_index


urlpatterns = [
    path('',index , name='index'),
    path('video/',video_index ,name='video')
]
