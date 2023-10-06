from rest_framework import serializers
from libraries.models import Library, Contacts, Coordinates

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"

class LibrariesSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=False)
    coordinates = CoordinatesSerializer(many=False)

    class Meta:
        model = Library
        fields = "__all__"
