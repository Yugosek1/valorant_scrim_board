from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
    def handle_no_permission(self):
        return redirect("scrim_detail", pk=self.kwargs["pk"])

class OwnProfileOnly(UserPassesTestMixin):
    def test_func(self):
        profile_obj = self.get_object()
        return profile_obj == self.request.user.profile