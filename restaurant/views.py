from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking , Menu
from .serializers import BookingSerializer, MenuSerializer
# Create your views here.


def index(request):
   return render(request,'index.html',{})

# class bookingView(APIView):

#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = MenuSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'success', 'data': serializer.data})
        

# class menuView(APIView):

#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = menuSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'success', 'data': serializer.data})
        

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

