from django.contrib import admin

# Register your models here.
from product.models import Principle, ProductCategory, Product, ProductSell

admin.site.register(Principle)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductSell)
