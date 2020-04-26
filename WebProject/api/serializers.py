from .models import Recipe, Categories
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('username', 'email', 'password',)
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ('id', 'name', 'recipes')
        read_only_fields = ['id']


class CategorySerializer2(serializers.Serializer):
    name = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)
        # return Categories.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', 'Not named Category')
        instance.save()
        return instance


class RecipeSerialier2(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    ingredients = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    rating = serializers.IntegerField()
    image = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)