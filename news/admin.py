from django.contrib import admin
from news.models import News, Comment, Video
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','created_at','category']
    ordering = ['-created_at','title']
    list_filter=['category','author']
    date_hierarchy='created_at'

class VideoAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-upload_at']

class CommentAdmin(admin.ModelAdmin):
    list_display=['news','create_at']

    ordering = ['-create_at']
    #list_filter=['category','reporter']
    date_hierarchy='news__created_at'

admin.site.register(News,NewsAdmin)  
admin.site.register(Comment,CommentAdmin)  
admin.site.register(Video,VideoAdmin)  
