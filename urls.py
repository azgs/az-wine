from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('azwine.views',
    url(r'^home/$', 'homepage'),
)

urlpatterns += patterns('',
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/home'})
)