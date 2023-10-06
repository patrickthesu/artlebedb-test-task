from rest_framework import viewsets
from libraries.models import Library
from libraries.serializers import LibrariesSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrariesSerializer
