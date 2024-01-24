from django.contrib import admin

from main.models import Link, Contacts, Product


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'provider', 'debt', 'created_at',)
    list_filter = ('contacts__city',)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'model', 'product_launch_date',)
