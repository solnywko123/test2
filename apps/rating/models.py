from django.db import models
from django.contrib.auth import get_user_model
from apps.comic.models import Comic

User = get_user_model()


class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'Too bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    id = models.AutoField(primary_key=True)
    comic_id = models.ForeignKey(Comic, related_name='ratings', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f"{self.user_id} --> {self.comic_id}"

