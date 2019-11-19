from rest_framework.viewsets import ModelViewSet

from app.models import Note, Client, Tag
from .serializers import (
    ClientSerializer,
    TagSerializer,
    NoteSerializerDetail,
    NoteSerializer
)


# Tags

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Client

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# Note

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializerDetail


class NoteViewSetStore(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
