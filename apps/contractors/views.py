from rest_framework.viewsets import ModelViewSet
from .models import Contractor
from .serializers import ContractorSerializer


class ContractorViewSet(ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
