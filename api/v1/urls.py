# builtin imports
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('auth/', include('api.v1.routes.auth')),
    path('docs/', include('api.v1.routes.docs')),
]