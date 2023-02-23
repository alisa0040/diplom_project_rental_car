from rest_framework.views import APIView, Response
from .models import Car, CarTransmission, CarModel, CarBrand, CarOption, CarImage, FuelType
from .serializers import CarModelSerializer, CarBrandSerializer, CarOptionSerializer, CarTransmissionSerializer, \
    CarSerializer
from .serializers import FuelTypeSerializer, CarImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListCreateAPIView


class CarBrandList(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarBrandDeleteView(DestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class CarModelList(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarModelDeleteView(DestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class FuelTypeList(ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarOptionList(ListCreateAPIView):
    queryset = CarOption.objects.all()
    serializer_class = CarOptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarOptionDeleteView(DestroyAPIView):
    queryset = CarOption.objects.all()
    serializer_class = CarOptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class CarApiview(APIView):
    def get(self, requests, id):
        car = get_object_or_404(Car, id=id)
        return Response(CarSerializer(car).data)


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class CarImageList(ListCreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarImageDeleteView(DestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class CarTransmissionList(ListCreateAPIView):
    queryset = CarTransmission.objects.all()
    serializer_class = CarTransmissionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarTransmissionDeleteView(DestroyAPIView):
    queryset = CarTransmission.objects.all()
    serializer_class = CarTransmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
