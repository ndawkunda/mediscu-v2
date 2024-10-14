# user-service/users/serializers.py
from rest_framework import serializers
from .models import HealthcareProfessional


class HealthcareProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareProfessional
        fields = ['id', 'username', 'email', 'specialization',
                  'verified', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = HealthcareProfessional.objects.create_user(**validated_data)
        return user
