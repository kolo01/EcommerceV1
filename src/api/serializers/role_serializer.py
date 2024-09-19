from base.models.role_model import RoleModel
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'