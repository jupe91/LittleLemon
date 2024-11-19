from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer



# Create your views here.
def index(request):
    return render(request, 'index.html')


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use the BookingSerializer
    permission_classes = [IsAuthenticated] 

# View for handling GET (list all) and POST (create) requests
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

# View for handling GET (retrieve), PUT (update), DELETE (destroy) requests for a single item
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
