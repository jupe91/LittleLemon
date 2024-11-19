from django.urls import path
from .views import MenuItemView, MenuItemDetailView

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu_items'),  # List and create items
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item_detail'),  # Detail view for a single item
]
