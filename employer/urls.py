from django.urls import path
from .views import EmployerList,EmployerDetailView

urlpatterns = [
    path('list/', EmployerList.as_view(), name='employer'),
    path('list/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
]