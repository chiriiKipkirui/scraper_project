from django.contrib import admin
from .models import Jumia, Avechi, Killmall, Products


class JumiaAdmin(admin.ModelAdmin):
    class Meta:
        model = Jumia
    list_display = ['product_id','product_price','product_warranty','product_discount','product_seller',
                    'timestamp','return_time']
    list_filter = ['product_id','product_seller']
    search_fields = ['product_id']


admin.site.register(Jumia, JumiaAdmin)


class AvechiAdmin(admin.ModelAdmin):
    class Meta:
        model = Avechi
    list_display = ['product_id','product_price', 'product_warranty', 'product_discount', 'product_seller',
                    'timestamp', 'return_time']
    list_filter = [ 'product_id','product_seller']
    search_fields = ['product_id']


admin.site.register(Avechi, AvechiAdmin)


class KillmallAdmin(admin.ModelAdmin):
    class Meta:
        model = Killmall

    list_display = ['product_id', 'product_price', 'product_warranty', 'product_discount', 'product_seller',
                    'timestamp', 'return_time']
    list_filter = ['product_id', 'product_seller']
    search_fields = ['product_id']


admin.site.register(Killmall, KillmallAdmin)


class ProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = Products
    list_filter = ['product_name','product_rating']
    search_fields = ['product_name']
    list_display = ['product_name','product_image','product_key_features']


admin.site.register(Products,ProductsAdmin)
