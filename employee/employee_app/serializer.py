from rest_framework import serializers
from .models import UserProfile

class EmployeeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    photo = serializers.ImageField(required=False, allow_empty_file=True, max_length=None)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        if 'photo' in validated_data:
            instance.photo = validated_data['photo']

        instance.save()
        return instance
