from rest_framework import serializers
from auths.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',) 
        
        
    def create(self, validated_data):
        password = self.validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token