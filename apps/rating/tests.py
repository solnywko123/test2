from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Rating
from ..comic.models import Comic

User = get_user_model()

# python manage.py test --keepdb запускать через эту команду, чтобы не удалялась авт бд

class ReviewerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.member = User.objects.create_user(username='anonymous', password='secretpass')
        self.story = Comic.objects.create(title='Fantastic Adventure')

    def test_submit_rating(self):
        data = {
            'comic_id': self.story.id,
            'user_id': self.member.id,
            'value': 4,
        }

        response = self.client.post('/api/ratings/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)
        self.assertEqual(Rating.objects.get().value, 4)

    def test_update_rating(self):
        existing_rating = Rating.objects.create(comic_id=self.story, user_id=self.member, value=3)
        data = {
            'comic_id': self.story.id,
            'user_id': self.member.id,
            'value': 5,
        }

        response = self.client.post('/api/ratings/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rating.objects.count(), 1)
        self.assertEqual(Rating.objects.get().value, 5)

    def test_average_rating(self):
        Rating.objects.create(comic_id=self.story, user_id=self.member, value=3)
        Rating.objects.create(comic_id=self.story, user_id=self.member, value=5)

        response = self.client.get(f'/api/comics/{self.story.id}/rating/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_rating'], 4.0)
