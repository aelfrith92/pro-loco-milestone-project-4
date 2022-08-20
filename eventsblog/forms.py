from .models import Comment
from django import forms


class CommentEventForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
