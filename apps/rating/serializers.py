from rest_framework import serializers

from apps.rating.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    product = serializers.ReadOnlyField(source='comic.title')

    class Meta:
        model = Rating
        fields = '__all__'

