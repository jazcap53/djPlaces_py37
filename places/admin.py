from django.contrib import admin

from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['city']

admin.site.register(Place, PlaceAdmin)
