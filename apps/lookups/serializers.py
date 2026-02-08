from rest_framework import serializers
from .models import (
    PriorityLevel,
    ProjectType,
    RoadType,
    DelayType,
    AlertType,
    BudgetSource,
    FiscalYear,
)


class BaseLookupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name"]


class PriorityLevelSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = PriorityLevel


class ProjectTypeSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = ProjectType


class RoadTypeSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = RoadType


class DelayTypeSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = DelayType


class AlertTypeSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = AlertType


class BudgetSourceSerializer(BaseLookupSerializer):
    class Meta(BaseLookupSerializer.Meta):
        model = BudgetSource


class FiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYear
        fields = ["id", "year_label"]
