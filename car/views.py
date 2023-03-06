from rest_framework.views import APIView, Response
from .models import Car, CarTransmission, CarModel, CarBrand, CarOption, CarImage, FuelType
from .serializers import CarModelSerializer, CarBrandSerializer, CarOptionSerializer, CarTransmissionSerializer, \
    CarSerializer
from .serializers import FuelTypeSerializer, CarImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.models import User
from employer.models import Employer

class CarBrandList(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarBrandDeleteView(DestroyAPIView):
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    def get_queryset(self):
        return CarBrand.objects.filter(is_employer__user=self.request.user)


class CarModelList(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarModelDeleteView(DestroyAPIView):
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    def get_queryset(self):
        return CarModel.objects.filter(is_employer__user=self.request.user)


class FuelTypeList(ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarOptionList(ListCreateAPIView):
    queryset = CarOption.objects.all()
    serializer_class = CarOptionSerializer
    permission_classes = [permissions.IsAuthenticated]



class CarOptionDeleteView(DestroyAPIView):
    serializer_class = CarOptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    def get_queryset(self):
        return CarOption.objects.filter(is_employer__user=self.request.user)



class CarApiview(APIView):
    def get(self, requests, id):
        car = get_object_or_404(Car, id=id)
        return Response(CarSerializer(car).data)
class CarList(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Car.objects.filter(is_employer__user=self.request.user)


class CarImageList(ListCreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarImageDeleteView(DestroyAPIView):
    serializer_class = CarImageSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return CarImage.objects.filter(is_employer__user=self.request.user)


class CarTransmissionList(ListCreateAPIView):
    queryset = CarTransmission.objects.all()
    serializer_class = CarTransmissionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarTransmissionDeleteView(DestroyAPIView):
    serializer_class = CarTransmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    def get_queryset(self):
        return CarTransmission.objects.filter(is_employer__user=self.request.user)
