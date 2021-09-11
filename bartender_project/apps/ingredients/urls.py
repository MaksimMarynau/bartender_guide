from django.urls import path

from .views import (
    category_create_view,
    category_detail_view,
    ingredient_list_view,
    ingredient_create_view,
    ingredient_detail_view
)

urlpatterns = [
    path('', ingredient_list_view, name='ingredient_list'),
    path('add', ingredient_create_view, name='ingredient_create'),
    path('detail/<str:slug>', ingredient_detail_view, name='ingredient_detail'),
    path('category/add', category_create_view, name='category_create'),
    path('category/<str:title_c>', category_detail_view, name='category_detail'),
]
