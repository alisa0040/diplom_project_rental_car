
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListCreateAPIView
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer


class ReservationList(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReservationUpdateView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReservationDeleteView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

