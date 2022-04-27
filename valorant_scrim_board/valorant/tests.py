from django.test import TestCase
from django.urls import reverse
from .models import Board

class ValorantTestCase(TestCase):
    def setUp(self):
        obj = Board(title="testTitle1", content="testContent1")
        obj.save()
    #日報の作成ができているか
    def test_saved_single_object(self):
        qs_counter = Board.objects.count()
        self.assertEqual(qs_counter, 1)
    
    #queryが存在しない時に、404ページを返すかどうか
    def test_response_404(self):
        detail_url = reverse('scrim_detail', kwargs={"pk": 100})
        detail_response = self.client.get(detail_url)
        update_url = reverse('scrim_update', kwargs={"pk": 100})
        update_response = self.client.get(update_url)
        delete_url = reverse('scrim_delete', kwargs={"pk": 100})
        delete_response = self.client.get(delete_url)
        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)

    #createページできちんとデータが保存されているか
    def test_create_on_createView(self):
        url = reverse('scrim_create')
        create_data = {"team_name": "scrim_from_test", "comment": "comment_from_test"}
        response = self.client.post(url, create_data)
        qs_counter2 = Board.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(qs_counter2, 2)