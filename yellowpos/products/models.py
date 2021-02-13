from django.db import models
from django.utils.translation import ugettext_lazy as _

from shops.models import Shop


class Category(models.Model):
    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    tax = models.FloatField(verbose_name=_('Tax'), default=0)
    tax_included = models.BooleanField(verbose_name=_('Tax included'), default=True)

    modified = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified'))
    order = models.IntegerField(verbose_name=_('Order'), default=255)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'), )

    class Meta:
        ordering = ('order',)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Text'))
    image = models.CharField(null=True, blank=True, max_length=250)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)

    price = models.FloatField(default=0, verbose_name=_('Sales Price'), )
    visible_web = models.BooleanField(default=True, verbose_name=_('Visible for web'), )

    archive = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified'))
