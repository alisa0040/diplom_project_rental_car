from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from employer.models import Employer
from employer.serializers import EmployerSerializer


class EmployerList(ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)

class EmployerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)
