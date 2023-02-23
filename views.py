from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.generics import UpdateAPIView, DestroyAPIView

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteView(DestroyAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    lookup_field = 'pk'


class CustomerUpdateView(UpdateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    lookup_field = 'pk'
