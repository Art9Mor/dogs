from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
