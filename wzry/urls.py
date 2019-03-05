from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^herolist', views.herolist, name='herolist'),
    url(r'^hero/(?P<nameNum>[0-9]+)/$', views.hero, name='hero'),
]