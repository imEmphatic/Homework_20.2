from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, products_details

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="product_list"),
    path("product/<int:pk>", products_details, name="products_details"),
]
