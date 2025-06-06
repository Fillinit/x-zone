from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from mainapp.views import change_language

urlpatterns = [
    path('change-language/<str:lang_code>/', change_language, name='change_language'),
]

urlpatterns += i18n_patterns(
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
