import decimal
import razorpay
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Profile

from .forms import RegistrationForm, AddressForm, ContactForm, LoginForm
from .models import Product, Category, Cart, Address, Order, CartItem, OrderItem, BlogPost

# Razorpay Client Initialization
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# ================================
# 🏠 General Views
# ================================

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def shop_view(request):
    products = Product.objects.filter(is_active=True, category__title__icontains="jewelry")
    return render(request, 'store/shop.html', {'products': products})

def test(request):
    return render(request, 'store/test.html')

# ================================
# 🛒 Cart Views
# ================================

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = sum(item.quantity * item.product.price for item in cart_items)
    shipping_amount = 10
    total_amount = grand_total + shipping_amount
    return render(request, 'store/cart.html', {
        'cart_products': cart_items,
        'grand_total': grand_total,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount,
        'amount': int(total_amount * 100),
        'addresses': Address.objects.filter(user=request.user),
    })

@login_required
def add_to_cart(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('store:cart')

@login_required
def remove_cart(request, cart_id):
    get_object_or_404(Cart, id=cart_id).delete()
    return redirect('store:cart')

@login_required
def plus_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.quantity += 1
    item.save()
    return redirect('store:cart')

@login_required
def minus_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    if item.quantity <= 1:
        item.delete()
    else:
        item.quantity -= 1
        item.save()
    return redirect('store:cart')

# ================================
# 💳 Checkout & Payment Views
# ================================

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    amount = sum(item.quantity * item.product.price for item in cart_items)
    shipping_amount = 10
    total_amount = amount + shipping_amount

    # Razorpay order create (not our db order)
    razorpay_order = razorpay_client.order.create({
        'amount': int(total_amount * 100),
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'cart_products': cart_items,
        'amount': int(total_amount * 100),
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount,
        'addresses': Address.objects.filter(user=request.user),
    }
    return render(request, 'store/checkout.html', context)



@login_required
def shop_checkout(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = 1

    amount = product.price * quantity
    shipping_amount = 10
    total_amount = amount + shipping_amount

    razorpay_order = razorpay_client.order.create({
        'amount': int(total_amount * 100),
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'product': product,
        'amount': int(total_amount * 100),
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount,
        'addresses': Address.objects.filter(user=request.user),
    }
    return render(request, 'store/checkout.html', context)

@csrf_exempt
def success(request):
    order_id = request.session.get('latest_order_id')
    order = Order.objects.filter(id=order_id).first()
    if order:
        send_mail(
            'Order Confirmation - Jewelry Shop',
            f"Thank you {order.user.username}, Order ID: {order.id}, Total: ₹{order.total_price}",
            settings.EMAIL_HOST_USER,
            [order.user.email],
        )
    return render(request, 'store/success.html', {'order': order})

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get("payment_id")
        address_id = request.POST.get("address_id")

        # Get Address
        address = get_object_or_404(Address, id=address_id, user=request.user)

        # Create New Order
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_amount=0,  # Temporary, below we will calculate
            payment_method="Online",
            status="Paid",
            is_paid=True,
            razorpay_payment_id=payment_id,
        )

        cart_items = Cart.objects.filter(user=request.user)

        total = 0
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
            total += item.product.price * item.quantity

        # Update the total amount after creating items
        shipping_amount = 10  # fixed shipping charge
        order.total_amount = total + shipping_amount
        order.save()

        # Clear Cart
        cart_items.delete()

        return render(request, 'store/payment_success.html', {'order': order})

    return redirect('store:home')


@csrf_exempt
def place_order(request):
    if request.method == "POST":
        address_id = request.POST.get('address_id')
        payment_method = request.POST.get('payment_method', 'COD')
        payment_id = request.POST.get('payment_id', '')

        # ✅ Check address id exist or not
        try:
            address = Address.objects.get(id=address_id, user=request.user)
        except Address.DoesNotExist:
            return redirect('store:checkout')  # If address not found, back to checkout.

        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return redirect('store:cart')

        amount = sum(item.quantity * item.product.price for item in cart_items)
        shipping_amount = 10
        total_amount = amount + shipping_amount

        # ✅ Create Order
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_amount=total_amount,
            payment_method=payment_method,
            is_paid=True if payment_method == "Online" else False,
            razorpay_payment_id=payment_id if payment_method == "Online" else "",
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        cart_items.delete()

        return render(request, 'store/payment_success.html', {'order': order})
    
    return redirect('store:home')


# ================================
# 🧾 Order Views
# ================================

@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': all_orders})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('orderitem_set__product')
    return render(request, 'store/order_history.html', {'orders': orders})

def order_success(request):
    return render(request, 'store/order_success.html')

# ================================
# 🛍️ Product & Category Views
# ================================

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/categories.html', context)

# ================================
# 📘 Blog Views
# ================================

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'store/blog_list.html', {'posts': posts})

def blog_post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'store/blog_detail.html', {'post': post})

# ================================
# 🧍‍♂️ User Authentication Views
# ================================

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!")
            return redirect('store:login')
        return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('store:home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('store:login')

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    profile = None
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    return render(request, 'store/profile.html', {
        'addresses': addresses,
        'orders': orders,
        'profile': profile
    })



@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('store:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/password_change.html', {'form': form})

# ================================
# 📍 Address Views
# ================================

@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'store/address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Address Added.")
            return redirect('store:checkout')
        return render(request, 'store/address.html', {'form': form})

@login_required
def remove_address(request, id):
    get_object_or_404(Address, id=id, user=request.user).delete()
    return redirect('store:checkout')




def update_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile = request.user.profile
        profile.profile_picture = request.FILES['profile_picture']
        profile.save()
    return redirect('store:profile')

def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    template_path = 'store/invoice.html'
    context = {'order': order}

    # HTML --> PDF convert
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
