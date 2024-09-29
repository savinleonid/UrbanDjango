from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('cart/', views.cart_page, name='cart_page'),
]
