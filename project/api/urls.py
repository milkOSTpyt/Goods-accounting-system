from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('category', CategoryViewSet, basename='category')
router.register('shops', ShopViewSet, basename='shops')
router.register('warehouse', WarehouseViewSet, basename='warehouse')
urlpatterns = router.urls

urlpatterns += [
    path('sold_out_product/', SoldOutProduct.as_view(),
         name='sold_out_product'),
]
