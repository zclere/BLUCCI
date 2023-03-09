from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('account.urls')),
    path('magazines/', include('magazine.urls')),
    path('options/', include('option.urls')),
#    path('about/', include('about.urls')),
#    path('siteinfo/', include('siteinfo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path('i18n/', include('django.conf.urls.i18n')),]