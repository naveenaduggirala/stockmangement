from django.contrib import admin
from .models import Stock,DailyMasters


class StockAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'products', 'qunatity','stoct_of_products')
    search_fields = ('products',)

    def get_actions(self, request):
        actions = super(StockAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False 


admin.site.register(Stock)
admin.site.register(DailyMasters)