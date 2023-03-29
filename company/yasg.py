from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title='Company API',
        default_version='v1',
        description='Documentation for Company API',
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpattern = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
