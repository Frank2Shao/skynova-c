# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('industry/', views.industry, name='industry'),
    path('support/',  views.support,  name='support'),
    path('news/',     views.news,     name='news'),
]
