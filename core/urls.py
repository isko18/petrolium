from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TEST API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@prolab.kg"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

front_urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('more/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('newPage/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('lab/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('leaders/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('news/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('price/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('prodaction_page/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('news/news_single/<int:id>/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('news/news_single/<int:id>/', TemplateView.as_view(template_name = 'index.html'), name = "index"),
]

api_urlpatterns = [
    path('swagger(^?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('apps.gallery.urls')),
    path('', include('apps.settings.urls')),
    path('news/', include('apps.news.urls')),
    path('team/', include('apps.team.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('', include(front_urlpatterns)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
