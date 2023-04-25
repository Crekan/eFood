from django.urls import path

from .views import RestaurantView, RestaurantDetailView, RestaurantCreateView

urlpatterns = [
    path('restaurants/', RestaurantView.as_view(), name='restaurants_view'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant/create/', RestaurantCreateView.as_view(), name='restaurant_create'),
]
