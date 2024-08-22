from django.contrib import admin
from .models import Caterory, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Caterory, CategoryAdmin)
# é da parte da ORM do django


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
    