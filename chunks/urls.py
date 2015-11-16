from django.conf.urls import *

urlpatterns = patterns('chunks.views',
    url(r'^(?P<slug>\w+)/edit/$', 'edit_link', name='edit_chunk'),
)
