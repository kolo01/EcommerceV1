from django.contrib import admin
from django.urls import path, include
from api.viewsets.cart_viewset import CartViewset
from api.viewsets.order_viewset import OrderViewset
from api.viewsets.paiement_viewset import PaiementViewset
from api.viewsets.product_viewset import ProductViewset
from api.viewsets.seller_viewset import SellerViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'order', OrderViewset)
router.register(r'cart', CartViewset)
router.register(r'paiement', PaiementViewset)
router.register(r'product', ProductViewset)
router.register(r'seller', SellerViewset)





urlpatterns = [
    path('', include(router.urls)),
]