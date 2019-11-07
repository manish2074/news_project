from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView , DetailView 
from django.db.models import Q
from news.models import News,Comment, Video
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.paginator import Paginator
# Create your views here.





class NewsTemplateView(TemplateView):
    template_name="index.html"
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news=News.objects.all()
        
        
        context["latest_news"] = news.order_by("-created_at") [:4]
        context["breaking_news"] = news.filter(Q(category="0")|Q(category="1")).order_by("-created_at") [:3]
        context["political_news"] = news.filter(category="0").order_by("-created_at") [:4]
        context["sports_news"] = news.filter(category="1").order_by("-created_at") [:4]
        context["health_news"] = news.filter(category="2").order_by("-created_at") [:4]
        context["business_news"] = news.filter(category="3").order_by("-created_at") [:4]
        context["international_news"] = news.filter(category="4").order_by("-created_at") [:4]
        context["finance_news"] = news.filter(category="5").order_by("-created_at") [:4]
        context["popular_news"] = news.order_by("-count")[:6]
       
        return context
    
   
class NewsCategoryView(ListView):
    model = News
    ordering =['-created_at']
    context_object_name ='category_list'
    template_name="news/category_news.html"
    paginate_by=2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get('category')
        return context

    def get_queryset(self):
        category = self.kwargs.get("category")
        category_key = [item[0] for item in News.CATEGORY if item[1] == category][0]
        return News.objects.filter(category=category_key)



class NewsDetailView(DetailView):
    model = News
    template_name='news/detail_news.html'
    context_object_name= 'news'
   
   
    def get_context_data(self, **kwargs):
        news=News.objects.all()
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news=self.object)
        context['popular_news'] = news.order_by("-count")[:6]

        # context["tags"] = TaggableManager().bulk_related_objects(self.object)
        self.object.count = self.object.count + 1
        self.object.save()
        return context


@login_required
def create_comment(request,**kwargs):
    data=request.POST
    news = get_object_or_404(News,pk=kwargs.get('pk'))
    feedback = data.get('feedback')
    comment_by = request.user
    payload = {"news":news,"comment_by":comment_by,"feedback":feedback}
    comment = Comment(**payload)
    comment.save()
    return render(request,"news/comment.html",{"comment":comment})

def news_search(request):
    searches = News.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        searches = searches.filter(title__icontains=search_term)  
    context={'search_term':search_term}
    return render(request,search.html,context)

def contact_us(request):
    template_name="contact.html"
    return render(request,template_name)
    
   
