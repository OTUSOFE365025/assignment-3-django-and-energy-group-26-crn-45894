from django.urls import path
from db import views as db_views

urlpatterns = [
    path('', db_views.product_lookup, name='product_lookup'),
    path('lookup-json/', db_views.product_lookup_json, name='product_lookup_json'),
]
