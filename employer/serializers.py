from rest_framework import serializers
from auths.models import User
from .models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
        read_only_fields = ('user', 'created_at')

