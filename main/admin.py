from django.contrib import admin

from main.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'debt', 'created_at')
    list_filter = ('city', )
