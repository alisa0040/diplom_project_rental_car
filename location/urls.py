from django.urls import path
from .views import LocationList, LocationCreateView, LocationDeleteView, LocationUpdateView,LocationDetailView

urlpatterns = [
    path('list/', LocationList.as_view(), name='location'),
    path('create/', LocationCreateView.as_view(), name='location-create'),
    path('list/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('list/<int:pk>/delete/', LocationDeleteView.as_view(), name='location-delete'),
    path('list/<int:pk>/update/', LocationUpdateView.as_view(), name='location-update'),
]