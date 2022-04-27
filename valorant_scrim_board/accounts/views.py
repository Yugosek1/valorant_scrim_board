from django.shortcuts import render
from .profile_forms import ProfileUpdateForm
from .models import Profile
from django.views.generic import UpdateView
from django.urls import reverse_lazy

class ProfileUpdateView(UpdateView):
    template_name = "accounts/profile_form.html"
    model = Profile
    form_class=ProfileUpdateForm
    success_url = reverse_lazy("scrim_list")