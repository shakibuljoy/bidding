from django.urls import path
from .views import show_comparison, create_comparison, show_list

app_name = 'tendering'

urlpatterns = [
    path('show-comparison/<pk>', show_comparison, name="show-comparison"),
    path('create', create_comparison, name="create-comparison"),
    path('', show_list, name="list"),
]
