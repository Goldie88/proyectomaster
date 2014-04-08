# Imports:
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sites.views.home', name='home'),
    #Site
    url(r'^apimonitors/', include('apimonitors.urls')),
    url(r'^apps/', include('apps.urls')),
    url(r'^banners/', include('banners.urls')),
    url(r'^calendars/', include('calendars.urls')),
    url(r'^chats/', include('chats.urls')),
    url(r'^directorys/', include('directorys.urls')),
    url(r'^forums/', include('forums.urls')),
    url(r'^geolocalizations/', include('geolocalizations.urls')),
    url(r'^hotels/', include('hotels.urls')),
    url(r'^jobboards/', include('jobboards.urls')),
    url(r'^magazines/', include('magazines.urls')),
    url(r'^netlabels/', include('netlabels.urls')),
    url(r'^newspapers/', include('newspapers.urls')),
    url(r'^photobooks/', include('photobooks.urls')),
    url(r'^pollings/', include('pollings.urls')),
    url(r'^radios/', include('radios.urls')),
    url(r'^realstates/', include('realstates.urls')),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^schools/', include('schools.urls')),
    url(r'^', include('sites.urls')),
    url(r'^stores/', include('stores.urls')),
    url(r'^tvs/', include('tvs.urls')),
    url(r'^userscontrols/', include('userscontrols.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
