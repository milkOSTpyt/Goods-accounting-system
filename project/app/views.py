from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView, LogoutView
from .models import Shop, Warehouse, Product, Category


class HomePage(View):
    """Главная страница сайта"""
    def get(self, request):
        return render(request, 'app/index.html')


class Shops(LoginRequiredMixin, ListView):
    """Вывод списка магазинов"""
    queryset = Shop.objects.all()
    template_name = 'app/shops.html'
    context_object_name = 'shops_list'
    extra_context = {'title': 'Магазины'}


class DetailShop(LoginRequiredMixin, ListView):
    """Вывод списка товаров определенного магазина"""
    template_name = 'app/detail_shop.html'
    context_object_name = 'shop_products'
    extra_context = {'title': 'Товары магазина'}
    paginate_by = 10

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Shop.objects.get(pk=self.kwargs['shop_id'])
        return context

    def get_queryset(self):
        return Product.objects.filter(shop_id=self.kwargs['shop_id'],
                                      sold_out=False).select_related('shop')


class Warehouses(LoginRequiredMixin, ListView):
    """Вывод списка складов"""
    queryset = Warehouse.objects.all()
    template_name = 'app/warehouses.html'
    context_object_name = 'warehouses_list'
    extra_context = {'title': 'Склады'}


class DetailWarehouse(LoginRequiredMixin, ListView):
    """Вывод списка товаров определенного склада"""
    template_name = 'app/detail_warehouse.html'
    context_object_name = 'warehouse_products'
    extra_context = {'title': 'Товары Склада'}
    paginate_by = 10

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Warehouse.objects.get(pk=
                                                 self.kwargs['warehouse_id'])
        return context

    def get_queryset(self):
        return Product.objects.filter(warehouse_id=self.kwargs['warehouse_id'],
                                      sold_out=
                                      False).select_related('warehouse')


class SoldOutProduct(LoginRequiredMixin, ListView):
    queryset = Product.objects.filter(sold_out=True)
    template_name = 'app/sold_out.html'
    context_object_name = 'sold_out_list'
    extra_context = {'title': 'Продано'}
    paginate_by = 10


class LoginUser(LoginView):
    """Вход"""
    form_class = AuthenticationForm
    template_name = 'app/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    """Регистрация"""
    form_class = UserCreationForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Регистрация'}


class LogoutUser(LogoutView):
    """Выход"""
    next_page = 'home'
