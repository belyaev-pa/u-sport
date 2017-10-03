# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from cart.cart import Cart
from .models import Product, ProductGroup, Setting, Order, OrderDetail
from .forms import Checkout

def home(request):    
  setting = Setting.objects.get(pk=1)    
  context = {               
    'setting': setting,
  }
  return render(request, 'main/home.html', context)

def group(request, group_id):
  setting = Setting.objects.get(pk=1)
  group_id = int(group_id)
  product_group = ProductGroup.objects.all()
  item_list = Product.objects.filter(group__id=group_id)
  context = {
    'group_id': group_id,
    'product_group': product_group,
    'item_list': item_list,
    'setting': setting,
  }
  return render(request, 'main/catalogue.html', context)
  
def catalogue(request):
  setting = Setting.objects.get(pk=1)
  product_group = ProductGroup.objects.all()
  item_list = Product.objects.all()
  context = {
    'product_group': product_group,
    'item_list': item_list,
    'setting': setting,
  }
  return render(request, 'main/catalogue.html', context)
  
def item(request, item_id):
  setting = Setting.objects.get(pk=1)
  item_id = int(item_id)
  item = Product.objects.get(pk=item_id)
  context = {
    'item': item,
    'setting': setting,
  }
  return render(request, 'main/item.html', context)
  
def delivery(request):
  setting = Setting.objects.get(pk=1)
  context = {
    'setting': setting,
  }
  return render(request, 'main/delivery.html', context)
  
def cart_show(request):
  setting = Setting.objects.get(pk=1)
  cart = Cart(request)    
  form = Checkout(request.POST or None)
  context = {
    'cart': cart,
    'setting': setting,
    'form': form,
  }
  return render(request, 'main/cart.html', context)
  
def cart_add(request, item_id):
  quantity = 1
  product = Product.objects.get(id=item_id)
  cart = Cart(request)
  cart.add(product, product.price, quantity)
  setting = Setting.objects.get(pk=1)
  item_id = int(item_id)
  item = Product.objects.get(pk=item_id)
  context = {
    'item': item,
    'setting': setting,
  }
  return render(request, 'main/item.html', context)
  
def cart_del(request, item_id):
  setting = Setting.objects.get(pk=1)
  product = Product.objects.get(id=item_id)
  cart = Cart(request)
  cart.remove(product)
  return HttpResponseRedirect(reverse('main:cart_show',)) 
  
def cart_incr(request, item_id):
  quantity = 1
  product = Product.objects.get(id=item_id)
  cart = Cart(request)
  cart.add(product, product.price, quantity)
  return HttpResponseRedirect(reverse('main:cart_show',)) 
  
def cart_decr(request, item_id):
  quantity = int(-1)
  product = Product.objects.get(id=item_id)
  cart = Cart(request)
  cart.add(product, product.price, quantity)
  return HttpResponseRedirect(reverse('main:cart_show',)) 
  
def checkout(request):
  setting = Setting.objects.get(pk=1)
  cart = Cart(request)
  if cart.count() == 0:
    return HttpResponseRedirect(reverse('main:home',))
  form = Checkout(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form_save = form.save(request)
    return HttpResponseRedirect(reverse('main:success',))
  else:
    return HttpResponseRedirect(reverse('main:cart_show',)) 
    
def success(request):
  setting = Setting.objects.get(pk=1)
  context = {
    'setting': setting,
  }
  return render(request, 'main/success.html', context)
