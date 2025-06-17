# skynova/views.py
from django.views import View
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from allauth.account import app_settings
import json
import re
from .models import News, Product, Solution
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
        'description': article.description,
        'image': article.image.url if article.image else None,
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
        'description': article.description,
        'image': article.image.url if article.image else None,
        'created_at': article.created_at,
        'updated_at': article.updated_at
    }
    return JsonResponse(data)

def product_list(request):
    """API endpoint to list all products"""
    products = Product.objects.all()
    data = [{
        'sku': product.sku,
        'id': product.id,
        'title': product.title,
        'price': str(product.price),
        'description': product.description,
        'image': product.image.url if product.image else None,
    } for product in products]
    return JsonResponse({'products': data})

def product_detail(request, sku):
    """API endpoint to get a single product by SKU"""
    product = get_object_or_404(Product, sku=sku)
    parameters = [{
        'key': param.key,
        'value': param.value
    } for param in product.parameters.all()]
    
    data = {
        'id': product.id,
        'sku': product.sku,
        'title': product.title,
        'price': str(product.price),
        'description': product.description,
        'image': product.image.url if product.image else None,
        'parameters': parameters
    }
    return JsonResponse(data)

def solution_list(request):
    """API endpoint to list all solutions"""
    solutions = Solution.objects.all()
    data = [{
        'id': solution.id,
        'title': solution.title,
        'price': str(solution.price),
        'description': solution.description,
        'image': solution.image.url if solution.image else None,
    } for solution in solutions]
    return JsonResponse({'solutions': data})

def solution_detail(request, solution_id):
    """API endpoint to get a single solution by ID"""
    solution = get_object_or_404(Solution, id=solution_id)
    suggested_products = [{
        'name': suggested.name,
        'note': suggested.note
    } for suggested in solution.suggested_products.all()]
    
    data = {
        'id': solution.id,
        'title': solution.title,
        'price': str(solution.price),
        'description': solution.description,
        'image': solution.image.url if solution.image else None,
        'suggested_products': suggested_products
    }
    return JsonResponse(data)

# ————————————————
# Authentication API Views for Popup Login
# ————————————————

@method_decorator(csrf_exempt, name='dispatch')
class AuthAPIView(View):
    """Base class for authentication API views"""
    
    def dispatch(self, request, *args, **kwargs):
        # Only allow POST requests for auth operations
        if request.method != 'POST':
            return JsonResponse({'error': 'Method not allowed'}, status=405)
        return super().dispatch(request, *args, **kwargs)
    
    def get_json_data(self, request):
        """Helper to parse JSON from request body"""
        try:
            return json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

class SignupAPIView(AuthAPIView):
    """API endpoint for user registration"""
    
    def post(self, request):
        data = self.get_json_data(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        email = data.get('email', '').strip().lower()
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')
        
        # Validation
        errors = {}
        
        if not email:
            errors['email'] = 'Email is required'
        elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            errors['email'] = 'Invalid email format'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email already registered'
        
        if not password1:
            errors['password1'] = 'Password is required'
        elif len(password1) < 8:
            errors['password1'] = 'Password must be at least 8 characters'
        
        if password1 != password2:
            errors['password2'] = 'Passwords do not match'
        
        if errors:
            return JsonResponse({'errors': errors}, status=400)
        
        try:
            # Create user
            user = User.objects.create_user(
                username=email,  # Use email as username
                email=email,
                password=password1
            )
            
            # Create EmailAddress record for allauth
            email_address = EmailAddress.objects.create(
                user=user,
                email=email,
                primary=True,
                verified=False
            )
            
            # Send confirmation email
            send_email_confirmation(request, user, signup=True)
            
            return JsonResponse({
                'success': True,
                'message': 'Registration successful! Please check your email to verify your account.',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'is_verified': False
                }
            })
            
        except Exception as e:
            return JsonResponse({'error': f'Registration failed: {str(e)}'}, status=500)

class LoginAPIView(AuthAPIView):
    """API endpoint for user login"""
    
    def post(self, request):
        data = self.get_json_data(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')
        
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_active:
                # Check if email is verified (only if verification is mandatory)
                if app_settings.EMAIL_VERIFICATION == 'mandatory':
                    try:
                        email_address = EmailAddress.objects.get(user=user, email=email)
                        if not email_address.verified:
                            return JsonResponse({
                                'error': 'Please verify your email address before logging in.',
                                'needs_verification': True
                            }, status=403)
                    except EmailAddress.DoesNotExist:
                        return JsonResponse({
                            'error': 'Email verification required.',
                            'needs_verification': True
                        }, status=403)
                # For optional verification, allow login regardless of verification status
                
                # Login user
                login(request, user)
                
                # Check verification status
                is_verified = False
                try:
                    email_address = EmailAddress.objects.get(user=user, email=email)
                    is_verified = email_address.verified
                except EmailAddress.DoesNotExist:
                    is_verified = False
                
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful!',
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'is_verified': is_verified
                    }
                })
            else:
                return JsonResponse({'error': 'Account is disabled'}, status=403)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

class LogoutAPIView(View):
    """API endpoint for user logout"""
    
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'success': True, 'message': 'Logged out successfully'})
        else:
            return JsonResponse({'error': 'Not logged in'}, status=400)

class UserStatusAPIView(View):
    """API endpoint to check current user status"""
    
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({
                'authenticated': True,
                'user': {
                    'id': request.user.id,
                    'email': request.user.email,
                    'is_verified': EmailAddress.objects.filter(
                        user=request.user, 
                        verified=True
                    ).exists()
                }
            })
        else:
            return JsonResponse({'authenticated': False})

class ResendVerificationAPIView(AuthAPIView):
    """API endpoint to resend email verification"""
    
    def post(self, request):
        data = self.get_json_data(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        email = data.get('email', '').strip().lower()
        
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        
        try:
            user = User.objects.get(email=email)
            email_address = EmailAddress.objects.get(user=user, email=email)
            
            if email_address.verified:
                return JsonResponse({'error': 'Email is already verified'}, status=400)
            
            send_email_confirmation(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Verification email sent successfully!'
            })
            
        except (User.DoesNotExist, EmailAddress.DoesNotExist):
            return JsonResponse({'error': 'Email not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=500)

class CSRFTokenAPIView(View):
    """API endpoint to get CSRF token"""
    
    def get(self, request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})
