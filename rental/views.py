from datetime import datetime
from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from rental.models import Rental
from customer.models import Customer
from car.models import Car
from rental.serializers import RentalSerializer
from reservation.models import Reservation
from django.shortcuts import get_object_or_404
from rest_framework import generics
from users.permission import IsAdminUser


class RentalList(ListAPIView):
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.get(name=user.username)
        if user.is_staff:
            return Rental.objects.all()
        else:
            return Rental.objects.filter(customer=customer)

class RentalCreateView(CreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

class RentalDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.get(name=user.username)
        if user.is_staff:
            return Rental.objects.all()
        else:
            return Rental.objects.filter(customer=customer)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj
