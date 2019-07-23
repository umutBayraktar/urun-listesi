from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
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
