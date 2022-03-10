"""XXX_PROJECT_NAME_XXX URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from apps.accounts.views import exchange_token

urlpatterns = [
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/tracking/', include('apps.tracking.urls')),
    path('api/car/', include('apps.car.urls')),
    path('admin/', admin.site.urls),

    path('api/rest-auth/', include('rest_auth.urls')),
    re_path(r'api/social/(?P<backend>[^/]+)/$', exchange_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
