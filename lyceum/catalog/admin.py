from django.contrib import admin
import catalog.models

admin.site.register(catalog.models.Category)
admin.site.register(catalog.models.Tag)


# кастомная админка: регистрируем модель ITEM
@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.name.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)
