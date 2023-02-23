
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.generics import UpdateAPIView, DestroyAPIView

from employer.models import Employer
from employer.serializers import EmployerSerializer


class EmployerList(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)

class EmployerUpdateView(UpdateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Employer.objects.all()
    lookup_field = 'pk'

class EmployerDeleteView(DestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Employer.objects.all()
    lookup_field = 'pk'


