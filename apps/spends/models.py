from django.urls import reverse
from apps.users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):

    currency_iso_code = models.CharField(
        _("currency iso code"), max_length=3, blank=False, null=False, unique=True)
    symbol = models.CharField(
        _("symbol"), max_length=5, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

    def __str__(self):
        return self.currency_iso_code


class Category(models.Model):

    name = models.CharField(_("name"), max_length=50,
                            blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Spends(models.Model):

    name = models.CharField(_("name"), max_length=50,
                            blank=False, null=False)
    description = models.TextField(_("description"), blank=True, null=True)
    date_created = models.DateField(
        _("date created"), auto_now=True)
    amount = models.IntegerField(_("amount"), blank=False, null=False)
    category = models.ManyToManyField(
        Category, verbose_name=_("category"), blank=False)
    user = models.ForeignKey(User, verbose_name=_("user"),
                             on_delete=models.CASCADE, blank=False, null=False)
    currency = models.ManyToManyField(
        Currency, verbose_name=_("currency"),   blank=False)

    class Meta:
        verbose_name = _("Spend")
        verbose_name_plural = _("Spends")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Spends_detail", kwargs={"pk": self.pk})
