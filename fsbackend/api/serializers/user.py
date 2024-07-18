from rest_framework.serializers import ModelSerializer
from api.models.user import User


class UserSerializer(ModelSerializer):
    """
        Сериализатор для пользователей
    """
    class Meta:
        model = User
        fields = ['id', 'email']


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email', 'id']
        extra_kwargs = {'password': {'write_only': True}}
