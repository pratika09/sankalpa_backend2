from rest_framework import serializers
from .models import Chairperson


class ChairpersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chairperson
        fields = "__all__"
