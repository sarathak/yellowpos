from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.currencies import CURRENCY_CHOICES


class Shop(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200)
    currencu = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=settings.CURRENCY)
