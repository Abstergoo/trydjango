from django.shortcuts import render

from .forms import ProductForm, RawProductform
from .models import Products

def product_create_view(request):
    my_form = RawProductform()
    if my_form == RawProductform:
        my_form = RawProductform(request.POST)
    context = {
        'form' : my_form
    } 
    return render(request, "product/create.html", context)



def product_detail_view(request):
    obj = Products.objects.get(id=1)
    context = {
        'object ' : obj
    }
    return render (request, "product/detail.html", context)
# Create your views here.
