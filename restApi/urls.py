from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('voice', views.voice, name='voice'),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('v2/voice', views.voice, name='voice'),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('face', views.face, name='face'),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('v2/face', views.face, name='face'),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('mypage/emotion', views.mypage_emotion, name="mypage_emotion"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
