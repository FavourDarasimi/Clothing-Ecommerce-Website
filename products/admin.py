from django.contrib import admin
from products.models import Product,Comment,Category,Cart,CartItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Comment)
# Register your models here.
