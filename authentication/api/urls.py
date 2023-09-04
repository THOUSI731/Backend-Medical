from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('',views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserRegisterView.as_view(), name='auth_register'),
    path('home/', views.UserHomeView.as_view(), name='user_home'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
]