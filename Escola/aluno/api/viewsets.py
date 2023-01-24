from rest_framework import viewsets
from aluno.api import serializers
from aluno import models


class AlunoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlunoSerializer

    def get_queryset(self):
        ra = self.request.query_params.get('id', None)
        return models.Aluno.objects.filter(ra=ra)

    def create(self, request, *args, **kwargs):
        return super(AlunoViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(AlunoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(AlunoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(AlunoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(AlunoViewSet, self).destroy(request, *args, **kwargs)


class AlunoViewSetOut(viewsets.ModelViewSet):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializerOut
