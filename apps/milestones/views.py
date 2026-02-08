from rest_framework.viewsets import ModelViewSet
from .models import Milestone
from .serializers import MilestoneSerializer


class MilestoneViewSet(ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
