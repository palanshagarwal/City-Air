from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import location.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', location.views.ip_to_latlong, name='ip_to_latlong'),
    #url(r'^member/action$', allauthdemo.views.member_action, name='user_action'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
