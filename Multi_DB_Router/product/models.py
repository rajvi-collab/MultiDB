"""Product Model."""

from django.db import models

DATABASE = (
    ('data1_db', 'data1_db'),
    ('data2_db', 'data2_db'),
    ('data3_db', 'data3_db'),
    ('data4_db', 'data4_db'),
)


class ProductModel(models.Model):
    """Product model for details."""

    user = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    database = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """Meta Info."""

        app_label = 'product'
        verbose_name = 'ProductModel'
        verbose_name_plural = 'ProductModel'

    def __str__(self):
        """Return String."""
        return self.product_name
