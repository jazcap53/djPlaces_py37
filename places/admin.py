from django.contrib import admin

from .models import Place

# Register your models here.
# admin.site.register(Place)

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['city']

admin.site.register(Place, PlaceAdmin)
