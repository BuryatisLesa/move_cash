from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from app_cash.models import MoveCash
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
    template_name = "move_cash/move-cash-list.html"
    context_object_name = "movecashs"
    paginate_by = 5
    ordering = ["-created_at"]

class MoveCashDetail(DetailView):
    model = MoveCash
    template_name = "move_cash/move-cash-detail.html"
    context_object_name = "movecash"

class MoveCashCreate(LoginRequiredMixin, CreateView):
    model = MoveCash
    template_name = "move_cash/move-cash-create.html"
    form_class = MoveCashForm

    def form_valid(self, form):
        # проверка авторизации
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy("movecash_list")

class MoveCashUpdate(LoginRequiredMixin, UpdateView):
    model = MoveCash
    template_name = "move_cash/move-cash-create.html"
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
    template_name = "move_cash/move-cash-delete.html"


    def dispatch(self, request, *args, **kwargs):
        # проверка прав пользователя
        movecash = self.get_object()
        if movecash.user != request.user:
            raise PermissionDenied("У вас нет прав для удаление данной операции")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("movecash_list")
