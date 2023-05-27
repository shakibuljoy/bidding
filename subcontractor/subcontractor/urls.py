"""
URL configuration for subcontractor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tendering import views
from books.views import create_book, create_book_form, book_detail, delete_book, update_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/create_book', create_book, name="create-book"),
    path('htmx/create_form', create_book_form, name="htmx-book"),
    path('htmx/book/<pk>/', book_detail, name="detail-book"),
    path('htmx/delete/<pk>/', delete_book, name="delete-book"),
    path('htmx/update/<pk>/', update_book, name="update-book"),
    path('bidding/', include('tendering.urls'))
]
