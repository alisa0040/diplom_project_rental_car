from django.urls import path
from .views import RentalList, RentalCreateView,RentalDetailView

urlpatterns = [
    path('list/', RentalList.as_view(), name='rental'),
    path('create/', RentalCreateView.as_view(), name='rental-create'),
    path('list/<int:pk>/', RentalDetailView.as_view(), name='rental-detail'),
]