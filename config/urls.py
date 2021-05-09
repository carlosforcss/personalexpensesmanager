# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# Third Parties
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
# Project
from pem.users.urls import router as users_router


router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/users/", include(users_router.urls)),
    path("get_token/", auth_views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
