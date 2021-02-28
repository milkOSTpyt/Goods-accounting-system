from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('shops/', Shops.as_view(), name='shops'),
    path('shop/<int:shop_id>/', DetailShop.as_view(), name='shop'),
    path('warehouses/', Warehouses.as_view(), name='warehouses'),
    path('warehouse/<int:warehouse_id>/', DetailWarehouse.as_view(),
         name='warehouse'),
    path('sold_out/', SoldOutProduct.as_view(), name='sold_out'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]