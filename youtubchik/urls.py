from django.contrib import admin
from django.urls import path
from content.views import home_page, video_detail, add_video
from django.conf import settings
from django.conf.urls.static import static
from users.views import register_view, logout_view, login_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
    path('add_video', add_video, name='add_video'),
    path('signup', register_view, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)