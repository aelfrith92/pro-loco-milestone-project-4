from .models import Comment, Event
from django import forms
from django.utils import timezone


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

    # The form should allow to enter dates that are not too far. Validation
    # example available in the UpdateEvent view
    current_year = int((timezone.now()).strftime("%Y"))
    BIRTH_YEAR_CHOICES = [current_year, current_year+1]
    scheduled_on = forms.DateField(widget=forms
                                   .SelectDateWidget(years=BIRTH_YEAR_CHOICES))
