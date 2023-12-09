from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Rating, User
from ..comic.models import Comic
from .serializers import RatingSerializer
from ..comic.serializers import ComicSerializer

class RatingCreateAPIView(APIView):
    def post(self, request):
        comic_id = request.data.get('comic_id')
        user_id = request.data.get('user_id')
        value = request.data.get('value')

        try:
            comic = Comic.objects.get(pk=comic_id)
            user = User.objects.get(pk=user_id)
        except Comic.DoesNotExist:
            return Response({"error": "Комикс не найден"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        existing_rating = Rating.objects.filter(comic_id=comic_id, user_id=user_id).first()

        if existing_rating:
            # обновляем если уже ставил
            if value is not None:  # Проверяем, что значение не является None
                existing_rating.value = value
                existing_rating.save()
                return Response({"message": "Оценка успешно обновлена"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Значение не может быть None"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # создаем новую если нет
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicRatingAPIView(APIView):
    def get(self, request, comic_id):
        comic = get_object_or_404(Comic, pk=comic_id)
        ratings = comic.ratings.all()
        serializer = RatingSerializer(instance=ratings, many=True)
        average_rating = ratings.aggregate(Avg('value'))['value__avg']
        comic.rating = average_rating
        comic.save()

        return Response({"average_rating": average_rating}, status=status.HTTP_200_OK)

