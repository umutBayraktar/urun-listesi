from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Product

class ProductCreate(CreateView):

    model = Product
    fields = "__all__"
    template_name_suffix = "_create_form"



class ProductDetail(DetailView):

    model = Product


class ProductUpdate(UpdateView):

    model = Product
    fields = "__all__"
    template_name_suffix = "_update_form"

class ProductDelete(DeleteView):

    model = Product
    success_url = reverse_lazy('product:product_list')
