from django.urls import path
from .views import (
    HomeView, 
    ItemDetailView, 
    add_to_cart, 
    remove_from_cart, 
    CheckoutView, 
    OrderSummaryView,
    remove_single_item_from_cart,
    searchResult,
    add_to_cart_order_summary,
    remove_from_cart_order_summary
    )

app_name = 'base_app'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('add-item-to-cart/<slug>/',add_to_cart_order_summary, name='add-to-cart-order-summary'),
    path('remove-item-from-cart/<slug>/',remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('delete-from-cart/<slug>/',remove_from_cart_order_summary, name='remove-from-cart-order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('search/', searchResult, name='search')
]
