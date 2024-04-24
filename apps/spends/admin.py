from django.contrib import admin
from .models import Category, Spends, Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_iso_code', 'symbol')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SpendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'description',
                    'amount', 'date_created')


admin.site.register(Spends, SpendsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Currency, CurrencyAdmin)
