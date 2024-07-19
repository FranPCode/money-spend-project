"""Models for spends and spends atributes."""

from django.forms import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Currency(models.Model):
    """Model for currency."""

    iso_code = models.CharField(
        _("iso code"), max_length=3, blank=False, null=False, unique=True)
    symbol = models.CharField(
        _("symbol"), max_length=5, blank=False, null=False)

    valid_symbols = [
        "$",    # United States Dollar (USD)
        "€",    # Euro (EUR)
        "¥",    # Japanese Yen (JPY)
        "£",    # British Pound Sterling (GBP)
        "A$",   # Australian Dollar (AUD)
        "C$",   # Canadian Dollar (CAD)
        "CHF",  # Swiss Franc (CHF)
        "元",   # Chinese Yuan Renminbi (CNY)
        "kr",   # Swedish Krona (SEK)
        "NZ$",  # New Zealand Dollar (NZD)
        "₱",    # Philippine Peso (PHP)
        "₹",    # Indian Rupee (INR)
        "₽",    # Russian Ruble (RUB)
        "R$",   # Brazilian Real (BRL)
        "₩",    # South Korean Won (KRW)
        "S/.",  # Peruvian Sol (PEN)
        "฿",    # Thai Baht (THB)
        "₫",    # Vietnamese Dong (VND)
        "₪",    # Israeli New Shekel (ILS)
        "R",    # South African Rand (ZAR)
    ]

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

    def clean(self):
        if self.iso_code and not self.iso_code.isupper():
            raise ValidationError('Field must be upper.')

        if self.symbol and self.symbol not in self.valid_symbols:
            raise ValidationError('Must be a valid currency symbol.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.iso_code


class Category(models.Model):

    name = models.CharField(_("name"), max_length=50,
                            blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def clean(self):
        if self.name:
            self.name = self.name.capitalize()

    def save(self, *args, **kwargs):

        self.full_clean()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Spends(models.Model):
    """Model for spends."""
    title = models.CharField(
        _("name"),
        max_length=50,
        blank=False,
        null=False
    )
    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )
    date_created = models.DateField(
        _("date created"),
        auto_now=True
    )
    amount = models.DecimalField(
        _("Amount"),
        max_digits=1000,
        decimal_places=2
    )
    category = models.ForeignKey(
        "spends.Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        "spends.Currency",
        verbose_name=_("Currency"),
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Spend")
        verbose_name_plural = _("Spends")

    def clean(self):
        """Validate and clean the data."""
        if self.title:
            self.title = self.title.capitalize()

        if self.description:
            self.description = self.description.capitalize()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
