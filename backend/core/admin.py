from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import (
    News, Product, Parameter, Solution, SuggestedProduct
)

# -------------------- import-export resources --------------------
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('id',)
        fields = ('id', 'sku', 'title', 'price', 'description', 'image')

class SolutionResource(resources.ModelResource):
    class Meta:
        model = Solution
        import_id_fields = ('id',)
        fields = ('id', 'title', 'price', 'description', 'image')

class NewsResource(resources.ModelResource):
    class Meta:
        model = News
        import_id_fields = ('id',)
        fields = ('id', 'title', 'description', 'slug', 'created_at', 'image')

# -------------------- inlines --------------------
class ParameterInline(admin.TabularInline):
    model = Parameter
    extra = 1

class SuggestedInline(admin.TabularInline):
    model = SuggestedProduct
    extra = 2

# -------------------- admins --------------------
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display   = ('sku', 'title', 'price')
    search_fields  = ('sku', 'title')
    inlines        = [ParameterInline]

@admin.register(Solution)
class SolutionAdmin(ImportExportModelAdmin):
    resource_class = SolutionResource
    list_display   = ('title', 'price')
    search_fields  = ('title',)
    inlines        = [SuggestedInline]

@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    resource_class      = NewsResource
    list_display        = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}