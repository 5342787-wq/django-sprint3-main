# ice_cream/admin.py
from django.contrib import admin
from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'is_published',
        'category',
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    # filter_horizontal = ('category',)

# Регистрируем класс с настройками админки для моделей IceCream и Category:


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# Регистрируем модели Topping и Wrapper,
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Location)
