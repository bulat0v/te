from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete = models.DO_NOTHING, verbose_name='Бренд')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField()
    description = models.TextField(max_length= 1000, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Есть в наличии')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    def __str__(self):
        return self.title
