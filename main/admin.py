# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ProductGroup, Product, Photo, Setting, Order, OrderDetail

class ProductGroupAdmin(admin.ModelAdmin):
  model = ProductGroup
admin.site.register(ProductGroup, ProductGroupAdmin)

class PhotoInline(admin.TabularInline):
  model = Photo
  def get_extra(self, request, obj=None, **kwargs):
    extra = 5
    if obj:
      return extra - obj.photo_set.count()
    return extra
    
class ProductAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name']}),
    (None, {'fields': ['group'],}),
    (None, {'fields': ['description'],}),
    (None, {'fields': ['main_photo'],}),
    (None, {'fields': ['price'],}),
  ]
  inlines = [PhotoInline]
  list_filter = ['group']
  search_fields = ['name', 'description']
admin.site.register(Product, ProductAdmin)

class SettingAdmin(admin.ModelAdmin):
  model = Setting
admin.site.register(Setting, SettingAdmin)

class OrderDetailInline(admin.TabularInline):
  model = OrderDetail
  def get_extra(self, request, obj=None, **kwargs):
    extra = 0
    return extra
    
class OrderAdmin(admin.ModelAdmin):
  fieldsets = [ 
    (None, {'fields': ['name']}),
    (None, {'fields': ['phone'],}),
    (None, {'fields': ['ship_to'],}),
    (None, {'fields': ['comment'],}),
    (None, {'fields': ['totalprice'],}),    
  ]
  model = Order
  inlines = [OrderDetailInline]
  list_filter = ['registered']
  search_fields = ['name']
admin.site.register(Order, OrderAdmin)
