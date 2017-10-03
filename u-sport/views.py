from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models

def stest_redirect(request): 
    return HttpResponseRedirect(reverse('main:home'))  
