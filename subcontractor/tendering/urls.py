from django.urls import path
from .views import show_comparison, create_comparison, show_list, price_comparison

app_name = 'tendering'

urlpatterns = [
    path('show-comparison/<pk>', show_comparison, name="show-comparison"),
    path('create', create_comparison, name="create-comparison"),
    path('price', price_comparison, name="price-comparison"),
    path('', show_list, name="list"),
]
