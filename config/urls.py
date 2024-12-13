from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns: list = [
    path('admin/', admin.site.urls),  # Адмін панель
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Отримання токену
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Оновлення токену
    path('', include('api.urls')),  # Підключення всіх шляхів з додатку api
]
