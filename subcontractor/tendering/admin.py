from django.contrib import admin
from .models import ComparetiveStatement, Item, ItemPrice

# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item


class CS(admin.ModelAdmin):
    inlines = [ItemInline]


admin.site.register(ComparetiveStatement, CS)
admin.site.register(ItemPrice)


