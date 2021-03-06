from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^app/', include('app.foo.urls')),
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls)),

                       (r'^postform/', 'lovelyspam.views.postForm'),
                       (r'^targets/(?P<siteID>\S*)/$', 'lovelyspam.views.getTargets'),
                       (r'^description/(?P<siteID>\d*)/$', 'lovelyspam.views.getDescription'),
                       (r'^blurb/(?P<blurbID>\d*)/(?P<wordCount>\d*)/$', 'lovelyspam.views.getBlurb'),

                       (r'^post/(?P<targetID>\d*)/$', 'lovelyspam.views.doPost'),
)
