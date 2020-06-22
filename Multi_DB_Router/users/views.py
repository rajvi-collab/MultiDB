"""Views for login user."""
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, SignUpForm
from users.models import CustomUser


class LoginView(View):
    """Docstring for HomeView."""

    def get(self, request, *args, **kwargs):
        """To get Dashboard."""
        if not request.user.is_authenticated:
            return render(request, 'login.html', {'login': LoginForm()})
        return redirect('users:home')

    def post(self, request, *args, **kwargs):
        """To authenticate the user."""
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST.get("email"), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('users:home')
        return render(request, 'login.html', {'login': form})


class HomeView(LoginRequiredMixin, View):
    """Docstring for HomeView."""

    def get(self, request, *args, **kwargs):
        """To get Dashboard."""
        ctx = {}
        if request.user.is_superuser:
            signup = SignUpForm()
            if kwargs.get('id'):
                user = CustomUser.objects.get(id=kwargs.get('id'))
                signup = SignUpForm(instance=user)
                ctx['id'] = kwargs.get('id')
            ctx['signup'] = signup
            ctx['user_list'] = CustomUser.objects.filter(is_staff=False)
            return render(request, 'users.html', ctx)
        else:
            return redirect('product:product')

    def post(self, request, *args, **kwargs):
        """To save the product."""
        user_list = CustomUser.objects.filter(is_staff=False)
        form = SignUpForm(request.POST)
        if kwargs.get('id'):
            user = CustomUser.objects.get(id=kwargs.get('id'))
            form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if not kwargs.get('id'):
                user.set_password(request.POST.get("password"))
                send_mail(
                    'User created and Details About Login',
                    'Here are the Details regarging the Login to the website. Your Email is %s and your password is %s' %
                    (request.POST.get('email'), request.POST.get('password')),
                    'test@mailinator.com',
                    [request.POST.get('email')],
                    fail_silently=False,
                )
            user.save()
            messages.success(request, 'User successfully created.')
            return redirect('users:home')
        return render(request, 'users.html', {'user_list': user_list, 'signup': form, 'id': kwargs.get('id')})
