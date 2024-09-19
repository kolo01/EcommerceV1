

from api.serializers.role_serializer import RoleSerializer
from base.models.role_model import RoleModel
from rest_framework import viewsets


class RoleViewset(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = RoleModel.objects.all()