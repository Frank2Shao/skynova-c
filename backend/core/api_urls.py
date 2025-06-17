from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='api_news_list'),
    path('news/<slug:slug>/', views.news_detail, name='api_news_detail'),
    path('products/', views.product_list, name='api_product_list'),
    path('products/<slug:sku>/', views.product_detail, name='api_product_detail'),
    path('solutions/', views.solution_list, name='api_solution_list'),
    path('solutions/<int:solution_id>/', views.solution_detail, name='api_solution_detail'),
    
    # Authentication APIs for Popup Login
    path('auth/csrf/', views.CSRFTokenAPIView.as_view(), name='api_csrf_token'),
    path('auth/signup/', views.SignupAPIView.as_view(), name='api_signup'),
    path('auth/login/', views.LoginAPIView.as_view(), name='api_login'),
    path('auth/logout/', views.LogoutAPIView.as_view(), name='api_logout'),
    path('auth/status/', views.UserStatusAPIView.as_view(), name='api_user_status'),
    path('auth/resend-verification/', views.ResendVerificationAPIView.as_view(), name='api_resend_verification'),
] 