from rest_framework.viewsets import ModelViewSet
from .models import Road
from .serializers import RoadSerializer


class RoadViewSet(ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
