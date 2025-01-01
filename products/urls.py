from django.urls import path
from . import views
from products.views import (
    NewProductView,
    AddComment,
)
urlpatterns = [
    path("",views.home,name="home"),
    path("category/",views.category,name="Category"),
    path("products/<int:pk>",views.productview,name="products"),
    path("details/<int:pk>",NewProductView.as_view(),name="product_detail"),
    path('details/comment/<int:pk>',AddComment.as_view(),name='add_comment'),
    path("search_products",views.search_result,name="search_products"),
    path("mycart/",views.cart,name="cart_view"),
    path('add/<int:pk>',views.addToCart,name='add_to_cart'),
    path('add/quantity/<int:pk>',views.addQuantity,name='add_quantity'),
    path('subtract/quantity/<int:pk>',views.subtractQuantity,name='subtract_quantity'),
    path('remove/<int:pk>',views.remove,name='remove')

]