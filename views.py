from datetime import datetime
from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rental.models import Rental
from rental.serializers import RentalSerializer
from reservation.models import Reservation


class RentalList(ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]


class RentalCreateView(CreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]




class RentalUpdateView(UpdateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

class RentalDeleteView(DestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
