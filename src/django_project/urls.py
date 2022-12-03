from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('proj-int-iii-admin/', admin.site.urls),
    # path('accounts/', include("django.contrib.auth.urls")),
    # path('accounts/', include("accounts.urls")),
    path('accounts/', include("allauth.urls")),
    path('', include("pages.urls")),
    path('shelters/', include("shelters.urls")),
    # path('api/', include("shelters.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns



