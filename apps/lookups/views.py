from rest_framework import viewsets
from .models import (
    PriorityLevel,
    ProjectType,
    RoadType,
    DelayType,
    AlertType,
    BudgetSource,
    FiscalYear,
)
from .serializers import (
    PriorityLevelSerializer,
    ProjectTypeSerializer,
    RoadTypeSerializer,
    DelayTypeSerializer,
    AlertTypeSerializer,
    BudgetSourceSerializer,
    FiscalYearSerializer,
)


class PriorityLevelViewSet(viewsets.ModelViewSet):
    queryset = PriorityLevel.objects.all()
    serializer_class = PriorityLevelSerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class RoadTypeViewSet(viewsets.ModelViewSet):
    queryset = RoadType.objects.all()
    serializer_class = RoadTypeSerializer


class DelayTypeViewSet(viewsets.ModelViewSet):
    queryset = DelayType.objects.all()
    serializer_class = DelayTypeSerializer


class AlertTypeViewSet(viewsets.ModelViewSet):
    queryset = AlertType.objects.all()
    serializer_class = AlertTypeSerializer


class BudgetSourceViewSet(viewsets.ModelViewSet):
    queryset = BudgetSource.objects.all()
    serializer_class = BudgetSourceSerializer


class FiscalYearViewSet(viewsets.ModelViewSet):
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer
