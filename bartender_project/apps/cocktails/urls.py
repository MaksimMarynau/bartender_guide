from django.urls import path

from .api.views import (
    style_create_view,
    style_detail_view,
    cocktail_create_view,
    cocktail_list_view,
    cocktail_detail_view,
    review_create_view,
)

urlpatterns = [
    path('', cocktail_list_view, name='cocktail_list'),
    path('add', cocktail_create_view, name='cocktail_create'),
    path('detail/<str:slug>/', cocktail_detail_view, name='cocktail_detail'),
    path('create-review', review_create_view, name='review_create'),
    path('style/add', style_create_view, name='style_create'),
    path('style/<str:title_s>', style_detail_view, name='style_detail'),
]
