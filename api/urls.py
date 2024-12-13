from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
                       CategoryViewSet,
                       CreateUserView,
                       SavingViewSet,
                       SubcategoryViewSet,
                       TransactionViewSet,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'savings', SavingViewSet, basename='saving')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns: list = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),  # Включення маршрутів, сформовані router
]
