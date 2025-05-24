from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from app_cash.models import MoveCash



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

class MoveCashCreate(CreateView):
    model = MoveCash
    template_name = "move_cash/move-cash-create.html"
    form_class = None
    success_url = reverse_lazy("movecash_list")

class MoveCashUpdate(UpdateView):
    model = MoveCash
    template_name = "move_cash/move-cash-create.html"
    form_class = None
    success_url = reverse_lazy("movecash_list")


class MoveCashDelete(DeleteView):
    model = MoveCash
    template_name = "move_cash/move-cash-delete.html"
    success_url = reverse_lazy("movecash_list")
