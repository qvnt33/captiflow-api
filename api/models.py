from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Категорії витрат"""

    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Subcategory(models.Model):
    """Підкатегорії витрат"""

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

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
                                    null=True)

    date = models.DateField()
    note = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.date}: {self.category} -> {self.amount}'


class Saving(models.Model):
    """Заощадження (резервні кошти)"""

    SAVING_TYPES = [
        ('cash', 'Готівка'),
        ('bank', 'Банк'),
        ('crypto', 'Криптовалюта'),
    ]
    saving_type = models.CharField(max_length=100, choices=SAVING_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.saving_type} -> {self.amount}'
