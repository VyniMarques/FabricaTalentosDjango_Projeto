from estagio import models
from estagio.api import serializers
from rest_framework import viewsets


class EstagioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EstagioSerializer

    def get_queryset(self):
        estagio_id = self.request.query_params.get('id', None)
        return models.Estagio.objects.filter(id=estagio_id)

    def create(self, request, *args, **kwargs):
        return super(EstagioViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(EstagioViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(EstagioViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(EstagioViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(EstagioViewSet, self).destroy(request, *args, **kwargs)
