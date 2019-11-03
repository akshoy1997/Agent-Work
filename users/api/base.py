from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BaseSerializer(serializers.ModelSerializer):
    """
    Base V1 Serializer
    """
    pass


class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Base V1 Model ViewSet
    """
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)