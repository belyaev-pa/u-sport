# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^$', home, name='home'),
  url(r'^catalogue/$', catalogue, name='catalogue'),
  url(r'^group/(?P<group_id>[0-9]+)/$', group, name='group_show'),
  url(r'^item/(?P<item_id>[0-9]+)/$', item, name='item'),
  url(r'^cart/add/(?P<item_id>[0-9]+)/$', cart_add, name='cart_add'),
  url(r'^cart/del/(?P<item_id>[0-9]+)$', cart_del, name='cart_del'),
  url(r'^cart/incr/(?P<item_id>[0-9]+)$', cart_decr, name='cart_decr'),
  url(r'^cart/decr/(?P<item_id>[0-9]+)$', cart_incr, name='cart_incr'),
  url(r'^cart/show/$', cart_show, name='cart_show'),
  url(r'^delivery/$', delivery, name='delivery'),
  url(r'^checkout/$', checkout, name='checkout'),
  url(r'^success/$', success, name='success'),
]
