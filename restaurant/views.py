from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import MenuItemSerializer
from .models import MenuItem

# Create your views here.
def index(request):
    return render(request, 'index.html')

# View for handling GET (list all) and POST (create) requests
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# View for handling GET (retrieve), PUT (update), DELETE (destroy) requests for a single item
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
