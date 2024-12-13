from collections import OrderedDict

from .models import Category, Saving, Subcategory, Transaction
from django.contrib.auth.models import User
from rest_framework import serializers


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields: list[str] = ['id', 'title', 'category']
        extra_kwargs: dict[str, dict[str, bool]] = {
            'category': {'read_only': True},  # Поле тільки для читання
        }


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields: list[str] = ['id', 'title', 'subcategories']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields: list[str] = ['id', 'amount', 'category', 'subcategory', 'date', 'note', 'created_at', 'updated_at']

    def validate(self, data: OrderedDict) -> OrderedDict:
        # Перевірка, чи підкатегорія належить до вибраної категорії
        if data.get('subcategory') and data.get('subcategory').category != data.get('category'):
            raise serializers.ValidationError('Підкатегорія не відповідає вибраній категорії.')
        return data


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields: list[str] = ['id', 'saving_type', 'amount', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields: list[str] = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data: OrderedDict) -> OrderedDict:
        # Перевірка на збіг паролів
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Паролі не співпадають'})
        return data

    def create(self, validated_data: OrderedDict) -> OrderedDict:
        # Видалення поля confirm_password перед створенням
        validated_data.pop('confirm_password')
        user: User = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
