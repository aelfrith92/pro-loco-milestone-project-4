from .models import Comment, Event
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentEventForm(forms.ModelForm):
    '''
        This class creates instances of a form that will let the user submit
        their comment
    '''
    class Meta:
        '''
            Fields
        '''
        model = Comment
        fields = ('body',)


class SuggestEventForm(forms.ModelForm):
    '''
        This class creates instances of a form that will let the user submit
        their event suggestion. Needed info: title, picture, caption, actual
        description, date of the event
    '''
    class Meta:
        '''
            Fields
        '''
        model = Event
        fields = ('title', 'featured_image', 'text_preview', 'content', 'scheduled_on')

        widgets = {
            'content': SummernoteWidget()
        }

        labels = {
            'scheduled_on': 'Scheduled on (accepted format: YYYY-MM-DD)',
        }
