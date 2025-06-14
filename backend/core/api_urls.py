from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='api_news_list'),
    path('news/<slug:slug>/', views.news_detail, name='api_news_detail'),
] 