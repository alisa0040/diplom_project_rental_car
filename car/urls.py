
from django.urls import path
from .views import CarTransmissionList, FuelTypeList,CarList, CarImageList, CarImageDeleteView, CarTransmissionDeleteView, CarOptionList,CarDetailView, CarOptionDeleteView, \
    CarModelList, CarModelDeleteView, CarBrandList, CarBrandDeleteView,CarCreateView

urlpatterns = [
    path('cars/', CarList.as_view(), name='cars'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('car_model/', CarModelList.as_view(), name='car-model'),
    path('car_model/<int:pk>/delete/', CarModelDeleteView.as_view(), name='car-model-delete'),
    path('car_brand/', CarBrandList.as_view(), name='car-brand'),
    path('car_brand/<int:pk>/delete/', CarBrandDeleteView.as_view(), name='car-brand-delete'),
    path('car_image/',CarImageList.as_view(), name='car-image'),
    path('car_image/<int:pk>/delete/', CarImageDeleteView.as_view(), name='car-image-delete'),
    path('fuel_type/', FuelTypeList.as_view(), name='fuel-type'),
    path('transmission/', CarTransmissionList.as_view(), name='transmission'),
    path('transmission/<int:pk>/delete/', CarTransmissionDeleteView.as_view(), name='transmission-delete'),
    path('car_option/', CarOptionList.as_view(), name='car-option'),
    path('car_option/<int:pk>/delete/', CarOptionDeleteView.as_view(), name='car-option-delete'),
]

