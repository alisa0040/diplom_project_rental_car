from django.urls import path
from .views import CustomerList, CustomerDetailView

urlpatterns = [
    path('list/', CustomerList.as_view(), name='customer'),
    path('list/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]