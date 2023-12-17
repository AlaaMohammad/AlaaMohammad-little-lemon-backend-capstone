from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemsSerializer
from .models import MenuItems,Booking


# Create your views here.
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer


class SingleMenuItemView(RetrieveAPIView,DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = MenuItemsSerializer
