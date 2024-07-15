from django.contrib import admin
from django.urls import path
from content.views import home_page, video_detail, add_video
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
    path('add_video/', add_video, name='add_video'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)