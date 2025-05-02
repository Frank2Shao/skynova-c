# core/views.py
from django.shortcuts import render

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
