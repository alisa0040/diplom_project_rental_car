from django.urls import path
from .views import ReservationList,ReservationCreateView,ReservationDetailView

urlpatterns = [
    path('list/', ReservationList.as_view(), name='reservation'),
    path('create/', ReservationCreateView.as_view(), name='reservation-create'),
    path('list/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    # path('list/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),
    # path('list/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation-update'),
]