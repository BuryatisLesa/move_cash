from app_cash.models import MoveCash
from django import forms

class MoveCashForm(forms.ModelForm):
    class Meta:
        model = MoveCash
        fields = "__all__"
        widgets = {
            "created_at": forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            "status": forms.Select(attrs={"class": "form-control", "placeholder": "Выберите статус операции"}),
            "typeoperation": forms.Select(attrs={"class": "form-control", "placeholder": "Выберите тип операции"}),
            "category": forms.Select(attrs={"class": "form-control", "placeholder": "Выберите категорию"}),
            "subcategory": forms.Select(attrs={"class": "form-control", "placeholder": "Выберите подкатегорию"}),
            "sum_operation": forms.NumberInput(attrs={"min": 0, "step": 0.01, "class": "form-control", "placeholder": "Введите сумму"}),
            "comment": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите комментарий"})
        }
        labels = {
            "created_at": "Дата",
            "status": "Статус",
            "typeoperation": "Операция",
            "category": "Категория",
            "subcategory": "Подкатегория",
            "sum_operation": "Сумма",
            "comment": "Комментарий"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
