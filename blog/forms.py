# blog/forms.py

from django import forms
from .models import Comment

class CreateCommentForm(forms.ModelForm):
    '''A form to create Comment data.'''

    class Meta:
        '''associate this form witht he Comment model'''
        model = Comment
        # fields = ['article', 'author', 'text', ]
        # remove the article because we want to do this automagically
        fields = ['author', 'text', ]
