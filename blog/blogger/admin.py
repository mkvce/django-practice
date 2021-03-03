from django.contrib import admin
from blogger.models import Author, Category, Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)