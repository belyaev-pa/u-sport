# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import get_object_or_404 
from django.forms.formsets import formset_factory 
from .models import Product, Order, OrderDetail, Setting
from cart.cart import Cart

class Checkout(forms.ModelForm):
  class Meta:
  model = Order
  fields = ('name', 'phone', 'ship_to', 'comment',)
  widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control'}),
    'phone': forms.TextInput(attrs={'class': 'form-control'}),
    'ship_to': forms.Textarea(attrs={'class': 'form-control','rows': 4}),
    'comment': forms.Textarea(attrs={'class': 'form-control','rows': 10}),
  }
  def save(self, request):
    data = super(Checkout, self).save()
    cart = Cart(request)
    order = Order.objects.get(pk=self.instance.id)
    order.totalprice = cart.summary()
    order.save()
    for item in cart:
      product = get_object_or_404(Product, pk=item.object_id)
      details = OrderDetail(
        order=order,
        product=product,
        quantity=item.quantity,
        price=item.total_price,
      )
      details.save()
