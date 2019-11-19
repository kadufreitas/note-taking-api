from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import filters, generics, mixins

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

class NoteViewSetStore(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = NoteSerializerDetail
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text', 'tags__name']

    def get_queryset(self):
        queryset = Note.objects.all()
        tag_id = self.request.query_params.get('tag', None)
        if tag_id is not None:
            queryset = queryset.filter(tags__in=tag_id)
        return queryset
