from rest_framework.viewsets import ModelViewSet
from .models import Engineer
from .serializers import EngineerSerializer


class EngineerViewSet(ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
