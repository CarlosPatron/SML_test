from django.urls import reverse
from django.test import TestCase
from django.urls.base import resolve
from .views import home, board_topics
from .models import Board

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def testHomeUrlResolvesHomeView(self):
        view = resolve('/')
        print(view)
        self.assertEquals(view.func, home)

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django board.")
    
    def testBoardTopicViewSuccessStatusCode(self):
        url = reverse('board_topics', kwargs={"id": 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def testBoardTopicViewNotFoundStatusCode(self):
        url = reverse("board_topics", kwargs={"id": 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def testBoardTopicUrlResolvesBoardTopicView(self):
        view = resolve("/boards/1/")
        self.assertEquals(view.func, board_topics)
    
    def testHomeViewContainsLinkToTopicsPage(self):
        board_topics_url = reverse("boards_topics", kwargs={"id": self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))