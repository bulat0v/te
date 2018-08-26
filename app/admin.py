from django.contrib import admin

from app.models import Brand
from app.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
