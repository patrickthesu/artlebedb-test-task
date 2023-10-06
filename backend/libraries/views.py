from rest_framework import viewsets
from libraries.models import Library
from libraries.serializers import LibrariesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrariesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'fullAdress'] 
    filterset_fields = ['name', 'fullAdress', 'timezone']
