from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Money Spend API",
        default_version='v1',
        description="This API allows you to efficiently track your expenses by including key components such as the title or name of the expense, different categories to classify the expense (e.g., food, transportation, entertainment), the total amount spent, support for multiple currencies, and any additional details or notes regarding the expense. This structure helps in managing and analyzing your expenses effectively, providing a clear overview of your spending habits.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fjpc23022000@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.api.urls')),
    path('api/', include('apps.spends.api.urls')),
]
