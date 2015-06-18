from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from ecoselfie import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('selfie.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)