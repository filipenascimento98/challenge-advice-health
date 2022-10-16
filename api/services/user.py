from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User

from api.serializers.user import UsuarioSerializer


class UserService(GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
