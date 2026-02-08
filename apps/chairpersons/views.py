from rest_framework.viewsets import ModelViewSet
from .models import Chairperson
from .serializers import ChairpersonSerializer


class ChairpersonViewSet(ModelViewSet):
    queryset = Chairperson.objects.all()
    serializer_class = ChairpersonSerializer
