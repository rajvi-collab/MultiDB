"""Forms for Product."""
from django import forms
from product.models import ProductModel, DATABASE


class ProductForm(forms.ModelForm):
    """Established Business for Sale form."""

    class Meta:
        """Definition for this class."""

        model = ProductModel
        fields = ['product_name', 'product_description', 'database']

    def __init__(self, *args, **kwargs):
        """Override fields objects."""
        self.request = kwargs.pop('request')
        super(ProductForm, self).__init__(*args, **kwargs)
        database = DATABASE if self.request.user.is_staff else ((data, data) for data in self.request.user.database)
        self.fields['database'].required = True
        self.fields['database'] = forms.ChoiceField(choices=database)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label
            })
