from django.urls import path
from .views import (
    HomeView, 
    ItemDetailView,
    ReviewView, 
    add_to_cart, 
    remove_from_cart, 
    CheckoutView, 
    OrderSummaryView,
    remove_single_item_from_cart,
    searchResult,
    sell,
    store_managment,
    add_to_cart_order_summary,
    remove_from_cart_order_summary
    )

app_name = 'base_app'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/<slug>/review', ReviewView.as_view(), name='review'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('add-item-to-cart/<slug>/',add_to_cart_order_summary, name='add-to-cart-order-summary'),
    path('remove-item-from-cart/<slug>/',remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('delete-from-cart/<slug>/',remove_from_cart_order_summary, name='remove-from-cart-order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('sell/',sell, name='sell'),
    path('store-managment/', store_managment, name='store-managment'),
    path('search/', searchResult, name='search'),
]
