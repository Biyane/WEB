from api.models import  Company
from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False,allow_blank=True, max_length=100)
    description = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    def create(self, validated_data):
        # return Company.objects.create(**validated_data)
        return Company.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

