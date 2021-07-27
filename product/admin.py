from django.contrib import admin

from .models import Product, Category

admin.site.register(Category)
admin.site.register(Product)

#TODO:
# create categories: Smartphones(Samsung, Iphone, Xiaomi), Notebooks(MacBook, ASUS, Acer, Lenovo), Earphones
# по 5 продуктов на каждую категорию, на наушники
