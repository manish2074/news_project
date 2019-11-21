from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.

class News(models.Model):
    CATEGORY=(("0","Politics"),("1","Sports"),("2","Health"),("3","Business"),("4","International"),("5","Finance"))
    title=models.CharField(max_length=250)
    story= models.TextField()
    count= models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True , related_name='post_likes')
    video_url = models.URLField(max_length=270,null=True,blank=True)  #makemigrations garna baki xa
    category= models.CharField(choices=CATEGORY, max_length=2)
    slug=models.SlugField(max_length=270,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cover_image=models.ImageField(upload_to="uploads")
    author= models.CharField(max_length=100,null=True)
    video_image = models.ImageField(blank=True,null=True)
    video_title = models.CharField(max_length=250,blank=True,null=True)
    tags = TaggableManager()
    def get_absolute_url(self):
    
        return reverse("detail_news",kwargs={"category":self.get_category_display(), "pk":self.pk, "slug":self.slug})
    
  

       

    def __str__(self):
        return self.title

    def get_like_url(self):
        return reverse("like_toogle",kwargs={"slug":self.slug})



    class Meta:
        
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    news= models.ForeignKey(News,on_delete=models.CASCADE,related_name="news_comment") 
    comment_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    feedback = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class NewsAd(models.Model):
    ad_small_image = models.ImageField(upload_to="uploads",blank=True,null=True)
    ad_small_image_updated = models.DateTimeField(auto_now_add=True)
    ad_large_image = models.ImageField(upload_to="uploads",blank=True,null=True)
    ad_large_image_updated = models.DateTimeField(auto_now_add=True)
    ad_small_url = models.URLField(max_length=270,blank=True,null=True)
    ad_large_url = models.URLField(max_length=270,blank=True,null=True)

   
