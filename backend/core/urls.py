# core/urls.py
'''from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('industry/', views.industry, name='industry'),
    path('support/',  views.support,  name='support'),
    #path('news/',     views.news,     name='news'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    # 占位：登录注册页面，后面再替换为真正表单
    path('login/',  TemplateView.as_view(template_name='login.html'),  name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
]'''

# skynova/urls.py
from django.urls import path, include, re_path
from .views import SPAView

urlpatterns = [
    path('api/', include('core.api_urls')),
    re_path(r'^.*$', SPAView.as_view()),
]