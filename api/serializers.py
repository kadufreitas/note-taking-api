from rest_framework import serializers

from app.models import Tag, Client, Note


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'client', 'title', 'text', 'tags')


class NoteSerializerDetail(serializers.ModelSerializer):
    client_name = serializers.StringRelatedField(source='client', read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = ('id', 'client_name', 'title', 'text', 'tags')
