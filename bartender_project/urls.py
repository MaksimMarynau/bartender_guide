from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


from .router import router


api_urls = [
    # path('account/', include('account.urls'), name='account_api'),
    path('cocktails/', include('cocktails.urls'), name='cocktails_api'),
    path('ingredients/', include('ingredients.urls'), name='ingredients_api'),
]

class ListApi(APIView):

    def get(self, request, format=None):
        api_urls = {
            'List-cocktails':'cocktails',
            'Create-cocktails':'cocktails/add',
            'Detail,Update,Delete-cocktails':'cocktails/detail/<str:slug>',
            'List-cocktail_ingredient':'cocktails/ingredients',
            'Create-cocktail_ingredient':'cocktails/ingredients/add',
            'Detail,Update,Delete-cocktail_ingredient':'cocktails/ingredients/detail/<int:pk>',
            'Create-style':'cocktails/style/add',
            'Detail,Update,Delete-style':'cocktails/style/<str:title_s>',
            'List-ingredients':'ingredients',
            'Create-ingredients':'ingredients/add',
            'Detail,Update,Delete-ingredients':'ingredients/detail/<str:slug>',
            'Create-category':'ingredients/category/add',
            'Detail,Update,Delete-category':'ingredients/category/<str:title_c>',
        }
        return Response(api_urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', ListApi.as_view()),
    path('api/', include(api_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
