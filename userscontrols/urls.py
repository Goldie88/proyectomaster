# Imports:
from django.conf.urls import patterns, include, url

urlpatterns = patterns('userscontrols.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^login/$', 'login', name='loginuser'),
    url(r'^newuser/$', 'newuser', name='newuser'),
    #url(r'^$', 'userscontrols2', name='userscontrols2'),
    #url(r'^userscontrols/$', 'userscontrols', name='userscontrols'),
)