from django.test import TestCase

class TestViews(TestCase):
    '''Test views via http response'''
    def test_get_event_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')
