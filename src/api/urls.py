from django.contrib import admin
from django.urls import path, include, re_path
from api.viewsets.cart_viewset import CartViewset
from api.viewsets.category_viewset import CategoryViewset
from api.viewsets.customer_viewset import CustomerViewset
from api.viewsets.order_viewset import OrderViewset
from api.viewsets.paiement_viewset import PaiementViewset
from api.viewsets.product_viewset import ProductViewset
from api.viewsets.role_viewset import RoleViewset
from api.viewsets.seller_viewset import SellerViewset
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'order', OrderViewset)
router.register(r'cart', CartViewset)
router.register(r'paiement', PaiementViewset)
router.register(r'product', ProductViewset)
router.register(r'seller', SellerViewset)
router.register(r'customer', CustomerViewset)
router.register(r'role', RoleViewset)
router.register(r'category', CategoryViewset)


schema_view = get_schema_view(
   openapi.Info(
      title="API ECOMMERCE",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]