from .models import Comment, Event
from django import forms


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
        fields = ('title', 'featured_image', 'text_preview', 'content',
                  'scheduled_on')

    BIRTH_YEAR_CHOICES = ['2022', '2023']
    scheduled_on = forms.DateField(widget=forms
                                   .SelectDateWidget(years=BIRTH_YEAR_CHOICES))

