"""Admin configuration for spends models."""
from django.contrib import admin
from .models import Category, Spends, Currency


class CurrencyAdmin(admin.ModelAdmin):
    """Admin configuration for Currency model."""
    list_display = ('id', 'iso_code', 'symbol')


class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""
    list_display = ('id', 'name')


class SpendsAdmin(admin.ModelAdmin):
    """Admin configuration for Spends model."""
    list_display = ('id', 'user', 'title', 'description',
                    'amount', 'date_created')


admin.site.register(Spends, SpendsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Currency, CurrencyAdmin)
