from rest_framework.viewsets import ModelViewSet
from .models import Alert
from .serializers import AlertSerializer


class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
