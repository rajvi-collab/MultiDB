"""Admin for product model."""
from django.contrib import admin

from .models import ProductModel


# class ProductModelFilter(admin.SimpleListFilter):
#     """Get product from all databases."""

#     def lookups(self, request, model_admin):
#         """Lookup."""
#         import pdb; pdb.set_trace()
#         product = set([c.country for c in model_admin.model.objects.all()])
#         return [c.product_name for c in product]
#         # You can also use hardcoded model name like "Country" instead of
#         # "model_admin.model" if this is not direct foreign key filter

#     def queryset(self, request, queryset):
#         """Queryset."""
#         if self.value():
#             return queryset.filter(country__id__exact=self.value())
#         else:
#             return queryset


# class ProductModelAdmin(admin.ModelAdmin):
#     """Product model admin."""

#     list_filter = (ProductModelFilter,)


# admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(ProductModel)
