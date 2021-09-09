from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from .router import router


api_urls = [
    # path('account/', include('account.urls'), name='account_api'),
    path('cocktails/', include('cocktails.urls'), name='cocktails_api'),
    path('ingredients/', include('ingredients.urls'), name='ingredients_api'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', include(api_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
