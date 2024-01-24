from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.models import Link, Contacts, Product


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'get_providers', 'debt', 'created_at',)
    list_filter = ('contacts__city',)
    actions = ('clear_debt',)
    list_display_links = ('get_providers',)

    def get_providers(self, obj):
        provider = obj.provider
        if provider:
            url = reverse('admin:main_link_change', args=[provider.id])
            return format_html('<a href="{}">{}</a>', url, provider.name)
        return '-'

    get_providers.short_description = 'Поставщик'

    @admin.action(description='Обнулить задолжность')
    def clear_debt(self, _, queryset):
        queryset.update(debt=0.00)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'model', 'product_launch_date',)
