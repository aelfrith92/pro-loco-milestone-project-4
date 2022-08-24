from django.test import TestCase
from .forms import CommentEventForm, SuggestEventForm
# Create your tests here.


class TestSuggestEventForm(TestCase):
    '''Testing required fields of the above'''
    def test_event_title_is_required(self):
        form = SuggestEventForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())

        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_event_content_is_required(self):
        form = SuggestEventForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())

        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_event_image_is_required(self):
        form = SuggestEventForm({'featured_image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('featured_image', form.errors.keys())

        self.assertEqual(form.errors['featured_image'][0], 'This field is required.')

    def test_event_scheduled_on_is_required(self):
        form = SuggestEventForm({'scheduled_on': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('scheduled_on', form.errors.keys())

    def test_explicit_fields_in_metaclass(self):
        form = SuggestEventForm()
        self.assertEqual(form.Meta.fields, ('title', 'featured_image', 'text_preview', 'content', 'scheduled_on'))

class TestCommentEventForm(TestCase):
    '''Testing required fields of the above'''
    def test_comment_body_is_required(self):
        form = CommentEventForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())

        self.assertEqual(form.errors['body'][0], 'This field is required.')
