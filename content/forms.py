from django import forms
from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_title', 'video_content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
