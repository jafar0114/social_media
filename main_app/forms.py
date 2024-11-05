from django import forms
from .models import Tweet, Reply

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows' : 3, 'placeholder' : 'What\'s happening'})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs={'rows': 2, 'placeholder' : 'Write a reply...'})
        }