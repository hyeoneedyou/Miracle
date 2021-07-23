from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('health/', include('health.urls')),
    path('study/', include('study.urls')),
    path('book/', include('book.urls')),
    path('wakeup/', include('wakeup.urls')),
    path('free/', include('free.urls')),
    path('users/', include('users.urls')),
    # allauth
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
