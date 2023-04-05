from django.test import TestCase, Client
from .models import Snippet

c = Client()


class SnippetTest(TestCase):
    # def setUp(self):
    #     Snippet.objects.create(created='2023,4,5',
    #                            title='Повесть о тупейшем тесте',
    #                            code='21',
    #                            linenos=False,
    #                            language='russian',
    #                            style='fairy tale',
    #                            owner='Sobaka Sobakovna',
    #                            highlighted='Lorem Ipsum is simply dummy text of the printing and typesetting industry'
    #                            )
    #
    # def test_snippet_contains_owner(self):
    #     story = Snippet.objects.get(title='Повесть о тупейшем тесте')
    #     self.assertEqual(story.contains(), 'Отрывок "Повесть о тупейшем тесте"')

    def get_from_url(self):
        c.get('http://127.0.0.1:8000/api/snippets/')

        response = c.post('/api/snippets/')
        response.content
        response = c.get



# Create your tests here.
