from django.contrib import admin
from django.utils.html import format_html
from .models import Address, Category, Product, Cart, Order, OrderItem, BlogPost

# 📍 Address Admin
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('locality', 'city', 'state')
    list_per_page = 10

# 🗂️ Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10

# 🛍️ Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'category', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    search_fields = ('title', 'category__title')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10

# 🛒 Cart Admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__title')
    list_per_page = 20

# 🧾 Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'payment_method', 'status', 'is_paid', 'created_at', 'display_products')
    list_filter = ('status', 'is_paid', 'payment_method', 'created_at')
    search_fields = ('user__username',)
    list_per_page = 20

    def display_products(self, obj):
        items = obj.items.all()
        return ", ".join([f"{item.product.title} ({item.quantity})" for item in items])
    display_products.short_description = 'Ordered Products'

# 🛍️ OrderItem Admin
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__title')

# 📘 BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

# 🛠️ Registering Admins
admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
