from django.contrib import admin
from django.urls import path

from .classViews import CategoryListView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from .views import home_page, product_list, product_detail, create_product, update_product, delete_product

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:id>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>', ProductDeleteView.as_view(), name='delete_product'),

]