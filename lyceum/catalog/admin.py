from django.contrib import admin

# Register your models here.
import catalog.models


# @admin.register(catalog.models.Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         catalog.models.Item.name.field.name,
#     )
#     list_editable = ('name',)
#     list_display_links = ('id',)
admin.site.register(catalog.models.Category)
admin.site.register(catalog.models.Tag)
admin.site.register(catalog.models.Item)