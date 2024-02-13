from django.urls import path
from rest_framework import routers

from dogs import views

router = routers.DefaultRouter()
router.register(r'dog', views.DogViewSet)

urlpatterns = [
    path('breed/', views.BreedList.as_view(), name='breed_list'),
    path('breed/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breed/<int:pk>/', views.BreedDetail.as_view(), name='breed_detail'),
    path('breed/update/<int:pk>/', views.BreedUpdate.as_view(), name='breed_update'),
    path('breed/delete/<int:pk>/', views.BreedDelete.as_view(), name='breed_delete'),
] + router.urls
