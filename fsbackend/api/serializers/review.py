from rest_framework.serializers import ModelSerializer
from api.models import Review
from api.serializers.user import UserSerializer

class ReviewSerializer(ModelSerializer):
    """
        Сериализатор для отзывов
    """

    # Эти две строчки можно убрать, если необходимо получать только айди
    user_from = UserSerializer()
    user_to = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewUpdateSerializer(ModelSerializer):
    """
        Сериализатор для редактированя отзывов
    """
    class Meta:
        model = Review
        fields = ['rating', 'review_text', 'user_to']