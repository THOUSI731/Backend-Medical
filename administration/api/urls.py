from django.urls import path
from . import views


urlpatterns = [
    path('',views.UserListAPIView.as_view(),name='user_list'),
    path('user/<int:pk>/',views.UserUpdateAPIView.as_view(),name='user_update'),
]
