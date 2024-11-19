from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemView, MenuItemDetailView, BookingViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

# Define urlpatterns
urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu_items'),  # List and create items
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item_detail'),  # Detail view for a single item
    path('', include(router.urls)),  # Include the booking viewset URLs
]
