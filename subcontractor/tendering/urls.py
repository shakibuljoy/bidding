from django.urls import path
from .views import show_comparison, create_comparison, show_list, price_comparison, show_price

app_name = 'tendering'

urlpatterns = [
    path('show-comparison/<pk>', show_comparison, name="show-comparison"),
    path('show-price/<pk>', show_price, name="show-price"),
    path('create', create_comparison, name="create-comparison"),
    path('price/<pk>', price_comparison, name="price-comparison"),
    path('', show_list, name="list"),
]
