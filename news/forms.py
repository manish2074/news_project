from django import forms
from .models import News,Like

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields ="title","story","cover_image","category","video_url","video_image","tags"
        

# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         fields="like","liked_by","liked_news"

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields=["news_tag"]