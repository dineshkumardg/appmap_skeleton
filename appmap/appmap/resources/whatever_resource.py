from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import DjangoAuthorization


from appmap.models.whatever import Whatever

class WhateverResource(ModelResource):
    class Meta:
        queryset = Whatever.objects.all()
        list_allowed_methods = ['get', 'post']
        authorization = DjangoAuthorization()
        resource_name = 'whatever'
        filtering = { "title" : ALL }
