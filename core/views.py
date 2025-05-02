# core/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    return render(request, 'core/index.html')

def products(request):
    # TODO: 后续替换为数据库读取
    return render(request, 'core/products.html')

def industry(request):
    """行业解决方案页面"""
    return render(request, 'core/industry.html')

def support(request):
    """支持服务页面"""
    return render(request, 'core/support.html')

def news(request):
    """新闻合规页面"""
    return render(request, 'core/news.html')


def news_list(request):
    # Query all News objects
    qs = News.objects.all()

    # For the server-rendered list/detail pages:
    posts = qs

    # For client-side (Vue) JSON data:
    # Build a list of dicts with just the fields you need
    posts_data = list(qs.values('title','slug','summary','created_at'))

    return render(request, 'core/news_list.html', {
        'posts':       posts,
        'posts_data':  posts_data,
    })

def news_detail(request, slug):
    post = get_object_or_404(News, slug=slug)
    return render(request, 'core/news_detail.html', {'post': post})