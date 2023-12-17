from django.urls import path
from .views import index,MenuItemsView ,SingleMenuItemView

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('booking/', bookingView.as_view()),
    # path('menu/', menuView.as_view()),
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    
]
