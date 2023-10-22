from django import forms
from .models import Subscriber, Comment


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
