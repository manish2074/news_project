from django.urls import path
from news import views
urlpatterns =[
  
    path('<str:category>/',views.NewsCategoryView.as_view(),name='category_news'),
    path('<str:category>/<int:pk>/<str:slug>/',views.NewsDetailView.as_view(),name='detail_news'),
    path('<str:category>/<int:pk>/<str:slug>/like/',views.PostLikeToogle.as_view(),name='like_toogle'),
    path('<str:category>/<int:pk>/<str:slug>/comment/',views.create_comment,name='create_comment'),
   
    
   
    
]


 