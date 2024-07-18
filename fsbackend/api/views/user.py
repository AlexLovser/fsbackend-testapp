from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from api.models.user import User
from api.serializers.user import UserSerializer, UserCreateSerializer

from api.models.review import Review
from api.serializers.review import ReviewSerializer

from datetime import datetime, timedelta, timezone



class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def list(self, request: Request):
        """
            У обычного пользователя, есть возможность получить только себя
        """
        return Response(UserSerializer(request.user).data)
    

@api_view(['POST'])
def register(request, *args, **kwargs):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.create(**serializer.validated_data)
    user.set_password(serializer.validated_data['password'])
    user.save()

    data = serializer.data
    data['id'] = user.id

    return Response(
        data,
        status=status.HTTP_201_CREATED
    )