"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

import books.views as books_view

urlpatterns = [
    path('', books_view.index),
    path('books/', books_view.shows_books_list, name='books_list'),
    path('books/<pub_date>/', books_view.shows_books_list_pub_date, name='books_list_pub_date'),
    path('admin/', admin.site.urls),
]
