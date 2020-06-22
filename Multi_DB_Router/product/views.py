"""Views for Products.."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .models import ProductModel
from .forms import ProductForm


class ProductHomeView(LoginRequiredMixin, View):
    """Docstring for HomeView."""

    def get(self, request, *args, **kwargs):
        """To get Dashboard."""
        product_form = ProductForm(request=request)
        if kwargs.get('id'):
            product = ProductModel.objects.using(kwargs.get('data')).get(id=kwargs.get('id'))
            product_form = ProductForm(request=request, instance=product)
        product_sec = []
        databases = ['data1_db', 'data2_db', 'data3_db', 'data4_db'] if request.user.is_staff else request.user.database
        for database in databases:
            products_list = ProductModel.objects.using(database).filter(user=request.user.id)
            if request.user.is_staff:
                products_list = ProductModel.objects.using(database).all()
            for pro in products_list:
                product_sec.append((database, pro))
        return render(request, 'product.html', {"product": product_form, 'product_list': product_sec,
                      'id': kwargs.get('id'), 'data': kwargs.get('data')})

    def post(self, request, *args, **kwargs):
        """To save the product."""
        form = ProductForm(request.POST, request=request)
        if kwargs.get('id'):
            product = ProductModel.objects.using(kwargs.get('data')).get(id=kwargs.get('id'))
            form = ProductForm(request.POST, request=request, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user.id
            database = kwargs.get('data') if kwargs.get('data') else request.POST.get('database')
            product.save(using=database)
            messages.success(request, 'Product has been successfully added')
        return redirect('product:product')
