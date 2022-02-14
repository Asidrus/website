from django.contrib import admin
from .models import categorys, itemName, pages, blocks, params

@admin.register(categorys)
class categorysAdmin(admin.ModelAdmin):
    list_display = ("id","category")

@admin.register(itemName)
class itemNameAdmin(admin.ModelAdmin):
    list_display = ("id", "general_heading_items", 'id_params')

@admin.register(params)
class paramsAdmin(admin.ModelAdmin):
    list_display = ("id", "importance")
    
@admin.register(blocks)
class blocksAdmin(admin.ModelAdmin):
    list_display = ("id", "title_block", "on_page", "id_category")

@admin.register(pages)
class pagesAdmin(admin.ModelAdmin):
    list_display = ("title_link", "id_block")

