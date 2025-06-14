# skynova/views.py
from django.views import View
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import News
import os

class SPAView(View):
    def get(self, request, *args, **kwargs):
        # static/dist/index.html 是 Vite build 的产物
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'static', 'dist', 'index.html')
        return FileResponse(open(path, 'rb'))

def news_list(request):
    """API endpoint to list all news articles"""
    news = News.objects.all().order_by('-created_at')
    data = [{
        'id': article.id,
        'title': article.title,
        'slug': article.slug,
        'summary': article.summary,
        'created_at': article.created_at,
        'updated_at': article.updated_at
    } for article in news]
    return JsonResponse({'news': data})

def news_detail(request, slug):
    """API endpoint to get a single news article by slug"""
    article = get_object_or_404(News, slug=slug)
    data = {
        'id': article.id,
        'title': article.title,
        'slug': article.slug,
        'content': article.content,
        'summary': article.summary,
        'created_at': article.created_at,
        'updated_at': article.updated_at
    }
    return JsonResponse(data)
