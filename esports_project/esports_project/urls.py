from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('esports_app.url'))
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)