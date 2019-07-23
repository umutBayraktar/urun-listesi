from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Product

class ProductCreate(CreateView):

    model = Product
    fields = "__all__"
    template_name_suffix = "_create_form"
