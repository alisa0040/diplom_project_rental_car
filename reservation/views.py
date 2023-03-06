from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer
from django.shortcuts import get_object_or_404
from customer.models import Customer
from rest_framework import generics

class ReservationList(ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.get(name=user.username)
        return Reservation.objects.filter(customer=customer)

class ReservationCreateView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.get(name=user.username)
        return Reservation.objects.filter(customer=customer)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj

