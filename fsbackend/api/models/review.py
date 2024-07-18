from django.db import models

    
class RatingTypes(models.IntegerChoices):
    """
        Возможные варианты оценки
    """
    GREAT = (1, 'Great')
    SOME_PROBLEMS = (2, 'Some Problems')
    BAD = (3, 'Bad')


class Review(models.Model):
    """
        Модель отзыва сделанная пользователем о другом пользователе
    """
    user_from = models.ForeignKey('User', related_name='my_reviews', on_delete=models.CASCADE) # Отправитель отзыва
    user_to = models.ForeignKey('User', related_name='reviews_about_me', on_delete=models.CASCADE) # Получатель отзыва
    
    rating = models.IntegerField(choices=RatingTypes.choices) # Оценка пользователя
    review_text = models.TextField(max_length=5000) # Текст отзыва

    date = models.DateTimeField(auto_now_add=True) # Дата создания отзыва

    def __str__(self) -> str:
        return f"Review of <{self.user_from.id}> about <{self.user_to.id}> "
