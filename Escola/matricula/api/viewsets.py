from matricula.api import serializers
from rest_framework import viewsets
from matricula import models


class MatriculaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializer

    def get_queryset(self):
        matricula_id = self.request.query_params.get('id', None)
        return models.Matricula.objects.filter(id=matricula_id)

    def create(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).destroy(request, *args, **kwargs)


class MatriculaViewSetOut(viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializerOut

    def get_queryset(self):
        ra = self.request.query_params.get('ra')

        if ra is None:
            return models.Matricula.objects.all()
        else:
            return models.Matricula.objects.filter(alunos_ra=ra)
