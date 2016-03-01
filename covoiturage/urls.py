from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('basededonnee.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
