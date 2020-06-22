"""Common home view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View


class HomeView(LoginRequiredMixin, View):
    """Docstring for HomeView."""

    def get(self, request, *args, **kwargs):
        """To get Dashboard."""
        if request.user.is_superuser:
            return redirect('users:home')
        else:
            return redirect('product:product')
