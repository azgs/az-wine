from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('azwine.views',
    url(r'^home/$', 'homepage'),
)