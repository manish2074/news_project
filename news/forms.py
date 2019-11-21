from django import forms
from .models import News

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields ="title","story","cover_image","category","video_url","video_image"
        


