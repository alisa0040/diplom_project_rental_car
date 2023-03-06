from location.models import Location
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework import generics
from location.serializers import LocationSerializer
from customer.models import Customer


class LocationList(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationUpdateView(UpdateAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()


class LocationDeleteView(DestroyAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()


class LocationDetailView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'pk'
