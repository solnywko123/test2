from django.urls import path
from .views import RatingCreateAPIView, ComicRatingAPIView

urlpatterns = [
    path('ratings/', RatingCreateAPIView.as_view()),
    path('comics/<int:comic_id>/rating/', ComicRatingAPIView.as_view()),
]


