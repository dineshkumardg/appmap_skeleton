from django.conf.urls import patterns, include, url
from resources.whatever_resource import WhateverResource

whatever_resource = WhateverResource()

urlpatterns = patterns('',
   url(r'^api/', include(whatever_resource.urls)),
)
