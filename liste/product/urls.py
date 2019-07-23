from django.contrib import admin
from django.urls import path,include
from .views import ProductCreate,ProductDetail,ProductUpdate

app_name = "product"


urlpatterns = [
    path('create/',ProductCreate.as_view(),name="product_create"),
    path('detail/<int:pk>',ProductDetail.as_view(),name="product_detail"),
    path('update/<int:pk>',ProductUpdate.as_view(),name="product_update")

]
