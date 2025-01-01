from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from products.models import Product, Comment, Category, Cart, CartItem
from django.urls import reverse_lazy
from .forms import CommentForm


def home(request):
    new_product = Product.objects.filter(new=True)
    context = {
        "new_product": new_product
    }
    return render(request, "home.html", context)


def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(name__contains=searched)


        context = {
            'searched': searched,
            'product': product,
        }
        return render(request, 'search_result.html', context)
    else:
        return render(request, 'search_result.html', {})


def category(request):
    category = Category.objects.filter(status=0)
    context = {"category": category}
    return render(request, 'category.html', context)


def productview(request, pk):
    if Category.objects.filter(pk=pk, status=0):
        product = Product.objects.filter(category=pk)
        category = Category.objects.filter(pk=pk).first()

        context = {
            "product": product,
            "category": category,
        }

        return render(request, "product_view.html", context)


class NewProductView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "Detail"


class AddComment(CreateView):
    model = Comment
    template_name = "addcomment.html"
    form_class = CommentForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product

        return super().form_valid(form)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        cart.save()
        items = CartItem.objects.filter(cart=cart)
        length = 0
        total_cost = 0
        for item in items:
            quantity = item.quantity
            cost = item.cost
            length += quantity
            total_cost += cost
    context = {'items': items, 'cart': cart,'length':length,'total_cost':total_cost}
    return render(request, "cartview.html", context)


def addToCart(request, *args, **kwargs):
    customer = request.user
    cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
    product = get_object_or_404(Product, pk=kwargs.get('pk'))
    cartItems = CartItem.objects.filter(cart=cart)

    if not cartItems:
        cartItem = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cartItem.cost = cartItem.quantity * cartItem.product.price
        cartItem.save()
    else:
        for items in cartItems:
            if product == items.product:
                pass
            else:
                cartItem = CartItem.objects.create(product=product, quantity=1, cart=cart)
                cartItem.cost = cartItem.quantity * cartItem.product.price
                cartItem.save()
                break
    return redirect('cart_view')


def addQuantity(request, *args, **kwargs):
    cartItem = get_object_or_404(CartItem, pk=kwargs.get('pk'))
    cartItem.quantity += 1
    cartItem.cost = cartItem.quantity * cartItem.product.price
    cartItem.save()
    return redirect('cart_view')


def subtractQuantity(request, *args, **kwargs):
    cartItem = get_object_or_404(CartItem, pk=kwargs.get('pk'))
    cartItem.quantity -= 1
    if cartItem.quantity <= 0:
        cartItem.delete()
    else:
        cartItem.cost = cartItem.quantity * cartItem.product.price
        cartItem.save()
    return redirect('cart_view')


def remove(request,*args,**kwargs):
    cartItem = get_object_or_404(CartItem,pk=kwargs.get('pk'))
    cartItem.delete()
    return redirect('cart_view')


# Create your views here.
