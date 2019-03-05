from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^wzry/', include('wzry.urls')),
    url(r'^admin/', admin.site.urls),
]