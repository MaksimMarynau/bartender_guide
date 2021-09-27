from django.urls import path

from .api.views import create_user_view, manage_user_view


urlpatterns = [
    path('create/', create_user_view, name='create'),
    path('me/', manage_user_view, name='me'),
]
