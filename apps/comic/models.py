from django.db import models


class Comic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комиксы'
        verbose_name_plural = 'Комиксы'


