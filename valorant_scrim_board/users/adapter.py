from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def __init__(self, request=None):
        super().__init__(request)

    def get_login_redirect_url(self, request):
        # リダイレクトするurl
        return 'http://127.0.0.1:8000/'


from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy

class ValorantAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        if request.user.email == request.user.profile.username:
            return reverse_lazy("profile-update", kwargs={"pk": request.user.profile.pk})
        else:
            return super().get_login_redirect_url(request)