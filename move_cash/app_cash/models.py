from django.db import models

class MoveCash(models.Model):
    """Движение денежных средств"""
    created_at = models.DateTimeField()
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="status")
    typeoperation = models.ForeignKey("TypeOperation", on_delete=models.CASCADE, related_name="typeoperations")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="categories")
    subcategory = models.ForeignKey("SubCategory", on_delete=models.CASCADE, related_name="subcategories")
    sum_operation = models.FloatField()


    def __str__(self):
        return f"{self.status}|{self.typeoperation}|{self.category}=>{self.subcategory}|{self.sum_operation}"



class Status(models.Model):
    """Статус операции"""
    name_status = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


    def __str__(self):
        return f"{self.name_status}"

class TypeOperations(models.Model):
    """Тип операции(Пополнение/Списание)"""
    type_operation = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"{self.type_operation}"

class Category(models.Model):
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
        return f"{self.category}=>{self.category}"


