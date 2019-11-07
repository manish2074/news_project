from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class News(models.Model):
    CATEGORY=(("0","Politics"),("1","Sports"),("2","Health"),("3","Business"),("4","International"),("5","Finance"))
    title=models.CharField(max_length=250)
    story= models.TextField()
    count= models.IntegerField(default=0)
    category= models.CharField(choices=CATEGORY, max_length=2)
    slug=models.SlugField(max_length=270, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cover_image=models.ImageField(upload_to="uploads")
    author= models.CharField(max_length=100,null=True)
    
    def get_absolute_url(self):
    
        return reverse("detail_news",kwargs={"category":self.get_category_display(), "pk":self.pk, "slug":self.slug})
    

    def __str__(self):
        return self.title

    def slug(self):
        return slugify(self.title)

    class Meta:
        
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    news= models.ForeignKey(News,on_delete=models.CASCADE,related_name="news_comment") 
    comment_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    feedback = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Video(models.Model):
    video_image = models.ImageField(upload_to="uploads")
    title = models.CharField(max_length=270)
    video_url = models.URLField(max_length=270)
    upload_at = models.DateTimeField(auto_now_add=True)
     


   
