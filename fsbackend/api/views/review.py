from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.models import Review, User
from api.serializers.review import ReviewSerializer, ReviewUpdateSerializer, ReviewCreateSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'patch', 'delete', 'post']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'update':
            # Для того, чтобы обновлять можно было только определенные поля
            return ReviewUpdateSerializer
        elif self.action == 'create':
            return ReviewCreateSerializer
        else:
            return ReviewSerializer

    @action(detail=False, methods=['get'])
    def my_reviews(self, request: Request):
        mine = request.user.my_reviews.all()
        return Response(ReviewSerializer(mine, many=True).data)
    
    @action(detail=False, methods=['get'])
    def about_me(self, request: Request):
        reviews_about_me = request.user.reviews_about_me.all()
        return Response(ReviewSerializer(reviews_about_me, many=True).data)

    def create(self, request: Request, *args, **kwargs):
        if request.data['user_to'] == request.user.id:
            raise ValidationError("You are can't create a review about yourself")
        
        request.data['user_from'] = request.user.id
        
        return super().create(request, *args, **kwargs)

    # Данные методы переопределены, чтобы пользователь не мог удалять/редактировать чужие ревью

    def update(self, request: Request, *args, **kwargs):
        instance: Review = self.get_object()

        if instance is None:
            raise ValidationError('Review does not exist')
        
        if instance.user_from.id != request.user.id:
            raise ValidationError("You are not authorized to edit this review.")
        
        if request.data.get('user_to') == instance.user_from.id:
            raise ValidationError("Invalid value for user_to")
               
        return super().update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        instance: Review = self.get_object()

        if instance is None:
            raise ValidationError('Review does not exist')
        
        if instance.user_from.id != request.user.id:
            raise ValidationError("You are not authorized to delete this review.")
                       
        return super().delete(request, *args, **kwargs)