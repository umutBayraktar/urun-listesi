from django.contrib import admin
from django.urls import path,include
from .views import ProductCreate,ProductDetail,ProductUpdate,ProductDelete,ProductList

app_name = "product"


urlpatterns = [
    path('create/',ProductCreate.as_view(),name="product_create"),
    path('detail/<int:pk>',ProductDetail.as_view(),name="product_detail"),
    path('update/<int:pk>',ProductUpdate.as_view(),name="product_update"),
    path('delete/<int:pk>',ProductDelete.as_view(),name="product_delete"),
    path('list/',ProductList.as_view(),name="product_list"),

]
