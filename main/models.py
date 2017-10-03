# -*- coding: utf-8 -*-
from datetime import date, datetime
from django.db import models
from django.utils import timezone

class ProductGroup(models.Model):
  name=models.CharField('Название группы товаров', max_length=255)
  class Meta:
    ordering=['name']
    verbose_name='Группа товаров'
  def __str__(self):
    return u'%s' % (self.name)
    
class Product(models.Model):
  name=models.CharField('Наименование товара', max_length=255)
  group=models.ForeignKey(ProductGroup, verbose_name='Группа товара')
  description=models.TextField('Описание товара')
  main_photo=models.ImageField('Главное фото', blank=True)
  price=models.FloatField('Цена')
  class Meta:
    ordering=['name']
    verbose_name='Товар'
  def __str__(self):
    return u'%s' % (self.name)
    
class Photo(models.Model):
  photo=models.ImageField(_('Photo'), blank=True)
  description=models.TextField(_('Photo text'))
  product=models.ForeignKey(Product, verbose_name=_('Product'), blank=True)
  class Meta:
    verbose_name=_('Photo')
  
class Setting(models.Model):
  number1=models.CharField('моб (1 \?)', max_length=255, blank=True)
  number2=models.CharField('моб (2 \?)', max_length=255, blank=True)
  number3=models.CharField('моб (3 \?)', max_length=255, blank=True)
  number4=models.CharField('моб (4 \?)', max_length=255, blank=True)
  delivery=models.TextField('текст доставки', blank=True)
  about_us=models.TextField('описание о нас', blank=True)
  mail_to=models.CharField('почта для оповещений', max_length=255, blank=True)
  head=models.CharField('телефон главный (/?)', max_length=255, blank=True)
  sv=models.CharField('самовывоз', max_length=255, blank=True)
  nav_bar_head=models.CharField('название навигационной панели', max_length=255, blank=True)
  nav_bar_text=models.CharField('текст навигационной панели', max_length=255, blank=True)
  def __str__(self):
    return u'%s' % (self.id)
    
class Order(models.Model):
  name = models.CharField('Наименование заказа ?', max_length=80)
  phone = models.CharField('телефон заказчика', max_length=16)
  ship_to = models.TextField('адрес')
  comment = models.TextField('комментарий', blank=True, null=True)
  totalprice = models.FloatField('Цена', blank=True, null=True)
  registered = models.DateTimeField('дата заказа', auto_now_add=True)
  class Meta:
    verbose_name = 'Заказ'
  def __str__(self):
    return u'%s.%s' % (self.pk, self.name)
    
class OrderDetail(models.Model):
  order = models.ForeignKey(Order)
  product = models.ForeignKey(Product)
  quantity = models.PositiveIntegerField(default=0)
  price = models.FloatField()
  def __str__(self):
    return u'%s' % (self.product.name)
