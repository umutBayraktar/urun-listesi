from django.contrib import admin
from django.urls import path,include
from .views import ProductCreate

app_name = "product"


urlpatterns = [
    path('create/',ProductCreate.as_view(),name="product_create")

]
