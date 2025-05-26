from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from app_cash.models import MoveCash, Category, TypeOperation, SubCategory
from app_cash.forms import MoveCashForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class MoveCashList(ListView):
    model = MoveCash
    template_name = "move_cash/movecash_list.html"
    context_object_name = "movecashs"
    paginate_by = 5
    ordering = ["-created_at"]

class MoveCashDetail(DetailView):
    model = MoveCash
    template_name = "move_cash/movecash_detail.html"
    context_object_name = "movecash"

class MoveCashCreate(LoginRequiredMixin, CreateView):
    model = MoveCash
    template_name = "move_cash/movecash_create.html"
    form_class = MoveCashForm

    def form_valid(self, form):
        # проверка авторизации
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        
        type_id = self.request.POST.get("typeoperation")

        if type_id:
            try:
                type_operation = TypeOperation.objects.get(id=type_id)
                # Фильтруем категории по типу операции
                form.fields["category"].queryset = Category.objects.filter(type_operation=type_operation)
            except TypeOperation.DoesNotExist:
                pass
        category_id = self.request.POST.get("category")
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                # Фильтруем подкатегории по типу категорий
                form.fields["subcategory"].queryset = SubCategory.objects.filter(category=category)
            except TypeOperation.DoesNotExist:
                pass
        return form

    
    success_url = reverse_lazy("movecashs")

class MoveCashUpdate(LoginRequiredMixin, UpdateView):
    model = MoveCash
    template_name = "move_cash/movecash_create.html"
    form_class = MoveCashForm

    def dispatch(self, request, *args, **kwargs):
        # проверка прав пользователя
        movecash = self.get_object()
        if movecash.user != request.user:
            raise PermissionDenied("У вас нет прав для редактирование данной операции")
        return super().dispatch(request, *args, **kwargs)

    success_url = reverse_lazy("movecash_list")


class MoveCashDelete(LoginRequiredMixin, DeleteView):
    model = MoveCash
    template_name = "move_cash/movecash_delete.html"


    def dispatch(self, request, *args, **kwargs):
        # проверка прав пользователя
        movecash = self.get_object()
        if movecash.user != request.user:
            raise PermissionDenied("У вас нет прав для удаление данной операции")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("movecash_list")
