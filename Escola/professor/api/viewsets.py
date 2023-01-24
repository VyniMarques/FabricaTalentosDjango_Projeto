from professor.api import serializers
from rest_framework import viewsets
from professor import models


class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessorSerializer

    def get_queryset(self):
        professor_id = self.request.query_params.get('id', None)
        return models.Professor.objects.filter(id=professor_id)

    def create(self, request, *args, **kwargs):
        return super(ProfessorViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(ProfessorViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ProfessorViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ProfessorViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProfessorViewSet, self).destroy(request, *args, **kwargs)
