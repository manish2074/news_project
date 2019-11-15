from django.contrib import admin
from news.models import News, Comment , NewsAd
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','created_at','category']
    ordering = ['-created_at','title']
    list_filter=['category','author']
    date_hierarchy='created_at'

class CommentAdmin(admin.ModelAdmin):
    list_display=['news','create_at']

    ordering = ['-create_at']
    #list_filter=['category','reporter']
    date_hierarchy='news__created_at'

class  AdAdmin(admin.ModelAdmin):
    list_display=['ad_large_image_updated','ad_small_image_updated']

admin.site.register(News,NewsAdmin)  
admin.site.register(Comment,CommentAdmin)  
admin.site.register(NewsAd,AdAdmin)  
  
 
