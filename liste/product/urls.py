from django.contrib import admin
from django.urls import path,include
from .views import ProductCreate,ProductDetail

app_name = "product"


urlpatterns = [
    path('create/',ProductCreate.as_view(),name="product_create"),
    path('detail/<int:pk>',ProductDetail.as_view(),name="product_detail")

]
