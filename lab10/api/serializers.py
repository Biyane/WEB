from api.models import  Company, Vacancy
from rest_framework import serializers
from django.contrib.auth.models import User


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100, default='Some Name')
    description = serializers.CharField(required=False, default='Nichego')
    city = serializers.CharField(required=False, default='London')
    address = serializers.CharField(required=False, default='Turgut Ozala 70')

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
        # return Company.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)


