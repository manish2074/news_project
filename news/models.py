from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify



# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def get_detail_url(self):
        return reverse("news_tag",kwargs={"tag_name":self.name})

    def __str__(self):
        return self.name


class News(models.Model):
    CATEGORY=(("0","Politics"),("1","Sports"),("2","Health"),("3","Business"),("4","International"),("5","Finance"))
    title=models.CharField(max_length=250)
    story= models.TextField()
    count= models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag,related_name='our_tag')
    video_url = models.URLField(max_length=270, null=True)  #makemigrations garna baki xa
    category= models.CharField(choices=CATEGORY, max_length=2)
    slug=models.SlugField(max_length=270,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cover_image=models.ImageField(upload_to="uploads")
    author= models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    video_image = models.ImageField(null=True)
        
    def get_absolute_url(self):
    
        return reverse("detail_news",kwargs={"category":self.get_category_display(), "pk":self.pk, "slug":self.slug})
    
  
    

       

    def __str__(self):
        return self.title





    class Meta:
        
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    news= models.ForeignKey(News,on_delete=models.CASCADE,related_name="news_comment") 
    comment_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    feedback = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Like(models.Model):
    like = models.ForeignKey(News,on_delete=models.CASCADE,related_name='news_like')
    liked_by=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    liked_news = models.BooleanField(default=False)
    

class NewsAd(models.Model):
    ad_small_image = models.ImageField(upload_to="uploads",blank=True,null=True)
    ad_small_image_updated = models.DateTimeField(auto_now_add=True)
    ad_large_image = models.ImageField(upload_to="uploads",blank=True,null=True)
    ad_large_image_updated = models.DateTimeField(auto_now_add=True)
    ad_small_url = models.URLField(max_length=270,blank=True,null=True)
    ad_large_url = models.URLField(max_length=270,blank=True,null=True)

            

   
