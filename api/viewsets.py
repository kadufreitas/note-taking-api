from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import filters, generics, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Client

# class ClientViewSet(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]


# Note

class NoteViewSetStore(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
        Endpoin para DELETE, POST e PUT de notas, aceitando apenas indentificadores (pk) nos campos de relacionamento.

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
            Não precisa passar o client, ao estar logado a nota é criada para o usuario Autenticado

            """
        user = request._user
        dataRequest = request.data.copy()
        dataRequest['client'] = user.pk
        serializer = self.get_serializer(data=dataRequest)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
            Não precisa passar o client, ao estar logado a nota é criada para o usuario Autenticado

            """
        user = request._user
        dataRequest = request.data.copy()
        dataRequest['client'] = user.pk

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=dataRequest, partial=partial)
        # serializer = self.get_serializer(data=dataRequest)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class NoteList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
           Retorna a lista de Notes com os campos detalhados

           """
    serializer_class = NoteSerializerDetail
    filter_backends = [filters.SearchFilter]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'text', 'tags__name']

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(client=user.pk)
        tag_id = self.request.query_params.get('tag', None)
        if tag_id is not None:
            queryset = queryset.filter(tags__in=tag_id)
        return queryset


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_name': user.username
        })
