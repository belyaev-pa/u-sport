import datetime
from django import template

register = template.Library()

@register.filter
def increment(value):
  return int(value)+1
  
@register.filter
def drob3(value):
  return value % 3     
