from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('signup.urls' ,namespace='signup')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
