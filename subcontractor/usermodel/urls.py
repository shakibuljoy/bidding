from django.urls import path
from .views import signup, testuser, login_view, logout_view

app_name = 'usermodel'

urlpatterns = [
    path('sign-up', signup, name='sign-up'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('test', testuser)
]