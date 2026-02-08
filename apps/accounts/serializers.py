from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "user_id",
            "full_name",
            "email",
            "role",
            "is_active",
            "created_at",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Account
        fields = ["user_id", "full_name", "email", "password", "role"]

    def create(self, validated_data):
        return Account.objects.create_user(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            user_id=validated_data["user_id"],
            password=validated_data["password"],
            role=validated_data.get("role", "USER"),
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            email=data["email"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        data["user"] = user
        return data
