from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RegistrationView
from django.contrib.auth.views import LogoutView
from store import views as store_views

app_name = 'store'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop_view, name='shop'),  # 🛠 Changed name to 'shop' for clarity

    # Cart & Orders
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:prod_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-cart/<int:cart_id>/', views.remove_cart, name='remove-cart'),
    path('plus-cart/<int:cart_id>/', views.plus_cart, name='plus-cart'),
    path('minus-cart/<int:cart_id>/', views.minus_cart, name='minus-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:id>/', views.shop_checkout, name='shop_checkout'),
    path('place-order/', views.place_order, name='place-order'),
    path('success/', views.success, name='success'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('orders/', views.orders, name='orders'),
    path('order-history/', views.order_history, name='order_history'),
    path('download-invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),



    # User Profile
    path('profile/', views.profile, name='profile'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),


    # Categories & Products
    path('categories/', views.all_categories, name='categories'),
    path('category/<slug:slug>/', views.category_products, name='category-products'),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
     

    # Blog
    path('blog/', views.blog_list, name='blog-list'),
    path('blog/<int:id>/', views.blog_post_detail, name='blog_post_detail'),

    # Address
    path('address/', views.AddressView.as_view(), name='add-address'),
    path('remove-address/<int:id>/', views.remove_address, name='remove-address'),

    # Auth
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    # Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='password-reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

    # Optional
    path('order-success/', views.order_success, name='order-success'),
    path('test/', views.test, name='test'),
]
