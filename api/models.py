from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Категорії витрат"""

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        # Унікальність категорії для кожного користувача
        constraints: list = [
            models.UniqueConstraint(fields=['title', 'user'], name='unique_category_for_user'),
        ]

    def __str__(self) -> str:
        return self.title


class Subcategory(models.Model):
    """Підкатегорії витрат"""

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        # Унікальність підкатегорії для кожної категорії
        constraints: list = [
            models.UniqueConstraint(fields=['title', 'category'], name='unique_subcategory_for_category'),
        ]

    def __str__(self) -> str:
        return self.title


class Transaction(models.Model):
    """Усі фінансові операції"""

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    related_name='transactions',
                                    blank=True,
                                    null=True,
                                    )
    date = models.DateField()
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if self.note == '':
            self.note = None
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.date}: {self.category.title} -> {self.amount}'


class Saving(models.Model):
    """Заощадження (резервні кошти)"""

    SAVING_TYPES: list[tuple[str]] = [
        ('cash', 'Готівка'),
        ('bank', 'Банк'),
        ('crypto', 'Криптовалюта'),
    ]
    saving_type = models.CharField(max_length=100, choices=SAVING_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.saving_type} -> {self.amount}'
