from django.urls import path

from .views import (
    style_create_view,
    style_detail_view,
    cocktailingredient_list_view,
    cocktailingredient_create_view,
    cocktailingredient_detail_view,
    cocktail_create_view,
    cocktail_list_view,
    cocktail_detail_view
)

urlpatterns = [
    path('', cocktail_list_view, name='cocktail_list'),
    path('add/', cocktail_create_view, name='cocktail_create'),
    path('detail/<str:slug>/', cocktail_detail_view, name='cocktail_detail'),
    path('ingredients/', cocktailingredient_list_view, name='ci_list'),
    path('ingredients/add/', cocktailingredient_create_view, name='ci_create'),
    path('ingredients/detail/<str:title_i>/', cocktailingredient_detail_view, name='ci_detail'),
    path('style/add', style_create_view, name='style_create'),
    path('style/<str:title_s>', style_detail_view, name='style_detail'),
]
