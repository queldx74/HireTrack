"""
URL configuration for hiretrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings

# Only superusers can access Django's built-in admin.
# HireTrack staff admins use the custom Admin Dashboard instead.
admin.site.has_permission = lambda request: (
    request.user.is_active and request.user.is_superuser
)

handler403 = "applications.views.error_403"
handler404 = "applications.views.error_404"
handler500 = "applications.views.error_500"


urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=settings.STATIC_URL + "images/favicon.ico",
            permanent=True,
        ),
    ),
    path("admin/", admin.site.urls),
    path("", include("applications.urls")),
]