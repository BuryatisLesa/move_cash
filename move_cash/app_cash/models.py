from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MoveCash(models.Model):
    """Движение денежных средств"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movecashes")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="status")
    typeoperation = models.ForeignKey("TypeOperation", on_delete=models.CASCADE, related_name="typeoperations")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="categories")
    subcategory = models.ForeignKey("SubCategory", on_delete=models.CASCADE, related_name="subcategories")
    sum_operation = models.FloatField()
    comment = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "ДДС"
        verbose_name_plural = "Движение денежных средств"


    def __str__(self):
        return f"{self.id}"



class Status(models.Model):
    """Статус операции"""
    name_status = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


    def __str__(self):
        return f"{self.name_status}"

class TypeOperation(models.Model):
    """Тип операции(Пополнение/Списание)"""
    type_operation = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"{self.type_operation}"

class Category(models.Model):
    type_operation = models.ForeignKey("TypeOperation", on_delete=models.CASCADE, related_name="typecategories")
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"

class SubCategory(models.Model):
    """Подкатегория => Категории"""
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.name}"


