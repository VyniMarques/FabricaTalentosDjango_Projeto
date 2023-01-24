from disciplina.api import serializers
from rest_framework import viewsets
from disciplina import models


class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisciplinaSerializerOut2

    def get_queryset(self):
        disciplina_id = self.request.query_params.get('id', None)
        return models.Disciplina.objects.filter(id=disciplina_id)

    def create(self, request, *args, **kwargs):
        return super(DisciplinaViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(DisciplinaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(DisciplinaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(DisciplinaViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(DisciplinaViewSet, self).destroy(request, *args, **kwargs)


class DisciplinaViewSetOut(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializerOut
