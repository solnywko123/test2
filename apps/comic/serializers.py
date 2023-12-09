from django.db.models import Avg
from rest_framework import serializers
from apps.comic.models import Comic


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'

    def get_rating(self, instance):
        avg_rating = instance.ratings.aggregate(Avg('rating'))
        rating_count = instance.ratings.count()
        return {'average_rating': avg_rating['rating__avg'], 'rating_count': rating_count}
