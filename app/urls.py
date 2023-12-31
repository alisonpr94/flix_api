from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tools API",
        default_version='v1',
        description="API for managing tools",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="alisonrib17@gmail.com"),
        #license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('tools.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^.*$', RedirectView.as_view(url='swagger/', permanent=False)),
]