from .models import Category, Saving, Subcategory, Transaction
from .serializers import (
    CategorySerializer,
    RegisterSerializer,
    SavingSerializer,
    SubcategorySerializer,
    TransactionSerializer,
)
from django.db.models.manager import BaseManager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView


class CreateUserView(APIView):
    """Реєстрація нового користувача"""

    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Користувач створений успішно!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для категорій"""

    queryset: BaseManager[Category] = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes: list = [IsAuthenticatedOrReadOnly]
    ordering_fields: str = '__all__'
    ordering: list[str] = ['category']  # Сортування за замовчуванням

    def get_queryset(self) -> BaseManager[Category]:
        # Повертає категорії тільки для авторизованого користувача
        if self.request.user.is_anonymous:
            return Category.objects.none()
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        # Прив'язуємо категорію до поточного користувача
        serializer.save(user=self.request.user)


class SavingViewSet(viewsets.ModelViewSet):
    """CRUD для заощаджень"""

    serializer_class = SavingSerializer
    permission_classes: list = [IsAuthenticatedOrReadOnly]

    filter_backends: list = [DjangoFilterBackend]
    filterset_fields: list[str] = ['saving_type']
    ordering_fields: str = '__all__'
    ordering: list[str] = ['amount']  # Сортування за замовчуванням

    def get_queryset(self) -> BaseManager[Saving]:
        if self.request.user.is_anonymous:
            return Saving.objects.none()
        return Saving.objects.filter(user=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(user=self.request.user)


class SubcategoryViewSet(viewsets.ModelViewSet):
    """CRUD для підкатегорій"""

    serializer_class = SubcategorySerializer
    permission_classes: list = [IsAuthenticatedOrReadOnly]

    filter_backends: list = [DjangoFilterBackend]
    filterset_fields: list[str] = ['category']
    ordering_fields: str = '__all__'
    ordering: list[str] = ['category']  # Сортування за замовчуванням

    def get_queryset(self) -> BaseManager[Subcategory]:
        if self.request.user.is_anonymous:
            return Subcategory.objects.none()
        return Subcategory.objects.filter(category__user=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save()


class TransactionViewSet(viewsets.ModelViewSet):
    """CRUD для фінансових операцій"""

    serializer_class = TransactionSerializer
    permission_classes: list = [IsAuthenticatedOrReadOnly]

    filter_backends: list = [DjangoFilterBackend, OrderingFilter]
    filterset_fields: list[str] = ['category', 'subcategory']
    ordering_fields: str = '__all__'
    ordering: list[str] = ['category']  # Сортування за замовчуванням

    def get_queryset(self) -> BaseManager[Transaction]:
        if self.request.user.is_anonymous:
            return Transaction.objects.none()
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(user=self.request.user)
