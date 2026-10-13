
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Patient


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]

    def validate_email(self, value):
        email = value.lower().strip()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )
        return email

    def create(self, validated_data):
        email = validated_data["email"]
        return User.objects.create_user(
            username=email,
            **validated_data
        )


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email", "").lower().strip()
        password = attrs.get("password")

        from django.contrib.auth import authenticate

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )

        if not user or not user.is_active:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "address",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]