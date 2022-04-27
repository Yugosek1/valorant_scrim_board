from datetime import time
from django.shortcuts import render
from django.views.generic.base import View
from .models import Board
from .forms import  ScrimModelForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from utils.access_restrictions import OwnerOnly

from django.utils import timezone

class ScrimListView(ListView):
    template_name = "valorant/scrim_list.html"
    model = Board
    ordering = ['start_at']

    def get_queryset(self):
        print(timezone.now())
        return Board.objects.filter(start_at__gte=timezone.now())

class ScrimDetailView(DetailView):
    template_name = "valorant/scrim_detail.html"
    model = Board

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["site_name"] = "testval"
        return ctx

class ScrimCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "valorant/scrim_formclass.html"
    form_class = ScrimModelForm
    success_url = reverse_lazy("scrim_list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.user = self.request.user
    #     obj.save()
    #     return super().form_valid(form)
    
    # def get_form_kwargs(self):
    #     kwgs = super().get_form_kwargs()
    #     kwgs["user"] = self.request.user
    #     return kwgs

class ScrimUpdateFormView(OwnerOnly, UpdateView):
    template_name = "valorant/scrim_formclass.html"
    model = Board
    form_class = ScrimModelForm
    success_url = reverse_lazy("scrim_list")
    
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update"] = True 
        return context
    
    # def get_form_kwargs(self):
    #     kwgs = super().get_form_kwargs()
    #     kwgs["user"] = self.request.user
    #     return kwgs

class ScrimDeleteView(OwnerOnly, DeleteView):
    # template_name = "valorant/scrim_delete.html"
    model = Board
    success_url = reverse_lazy("scrim_list")

