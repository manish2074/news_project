from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView , DetailView ,RedirectView,CreateView,DeleteView,UpdateView
from django.db.models import Q
from news.models import News,Comment,NewsAd,Tag
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify


from news.forms import NewsCreateForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


from django.core.paginator import Paginator
# Create your views here.

class CreateNewsView(LoginRequiredMixin,CreateView):
    model = News
    login_url='/accounts/login'
    form_class=NewsCreateForm
    
    template_name='news/create_news.html'
    success_url=reverse_lazy('home')
    

    def form_valid(self,form):
        tag_list = []
        news = form.save(commit=False)
        title= form.cleaned_data['title']
        tags= form.cleaned_data['tags']
        tag_list = [Tag.objects.get_or_create(name=tag)[0] for tag in tags.split()]

        # news_tag=form.cleaned_data['news_tag']
        news.author = self.request.user
        news.slug = slugify(title)
        for tag in tag_list:
            news.tags.add(tag)
        news.save()
        return super(CreateNewsView,self).form_valid(form)


    def form_invalid(self,form):
        print (form.errors)
        return super(CreateNewsView,self).form_invalid(form)  




# @login_required
# def create_news(request):
#     if request.method == 'POST':
#         n_form = NewsCreateForm(request.POST)
#         t_form = TagForm(request.POST)
#         if n_form.is_valid() and t_form.is_valid():
#             news = n_form.save(commit=False)
            
#             title= n_form.cleaned_data['title']
#             news.author = self.request.user
#             news.slug = slugify(title)
#             tags = t_form.save(commit=False)
#             news_tag = t_form.cleaned_data['news_tag']

            
#             news.save()
#             tags.save()
           
#             return redirect('home')
#     else:
#         n_form = NewsCreateForm()
#         t_form = TagForm()
        
#     context = {
#         'n_form':n_form,
#         't_form':t_form
#     }
#     return render(request,'news/create_news.html', context)
            





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
        context["video_news"] = news.order_by("-created_at") [:3]
        context["popular_news"] = news.order_by("-count")[:6]
       
        return context

class NewsAdView(ListView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads=NewsAd.objects.all()

        context["small_ads"] = ads.order_by("ad_small_image_updated") [:1]
        context["large_ads"] = ads.order_by("ad_large_image_updated") [:1]

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
        tags=self.object.tags.all()
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news=self.object)
        #context['my_likes'] = Like.objects.filter(news=self.object)
        context['popular_news'] = news.order_by("-count")[:6]
        context['tags'] = tags
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

# @login_required
# def create_like(request,**kwargs):
    
#     like= get_object_or_404(News,pk=kwargs.get('pk'))
#     liked_news=Like.objects.filter(liked_news=True)
#     liked_by=request.user
#     context = {
#         'like': like,
#         'liked_news':liked_news,
#         'liked_by':'liked_by'
#     }

#     liked_objects = Like(**context)
#     liked_objects.save()
#     return render(request,"news/like.html",{"liked_objects":liked_objects})
    


def contact_us(request):
    template_name="contact.html"
    return render(request,template_name)
    

class SearchResultsView(ListView):
    model = News
    template_name = 'search_results.html'    
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(Q(title__icontains=query))
        if query in object_list:
            return object_list
        else:
            return HttpResponse('there is no match for your search.') 


class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model = News
    template_name="news/update_news.html"
    fields = ("title","story")
    success_url=reverse_lazy("home")

class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    
    success_url=reverse_lazy("home")

def view_tag(request,tag_name):
    tag= Tag.objects.get(name=tag_name)
      
    news= tag.our_tag.all()
    return render(request,'news/tags.html',{"tag_name":tag_name,'news':news})  